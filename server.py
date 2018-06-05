# -*- coding: utf-8 -*-

import sys
import struct
import traceback
import message_pb2
import player_pb2
import importlib
from pb import header_pb2
from gevent.server import StreamServer

LENGTH_HEADER = '!I'
HEADER_LENGTH = struct.calcsize(LENGTH_HEADER)

def recv_fill(sock, packet_len):
    buff = ''
    while len(buff) < packet_len:
        try:
            data = sock.recv(packet_len - len(buff))
            if not data:
                return None
            buff += data
        except Exception as e:
            traceback.print_exc()
            return None
    return buff

socks = list()

def quit_conn(sock, name):
    socks.remove(sock)
    sock.close()
    msg = message_pb2.Message()
    player = msg.player
    player.id = 0
    player.name = '管理员'
    msg.content = u'%s 退出了聊天室' % (name,)
    data = msg.SerializeToString()
    packet_len = struct.pack(LENGTH_HEADER, len(data))
    for item in socks:
        item.sendall(packet_len + data)


def recv(sock, addr):
    socks.append(sock)
    while True:
        _len = recv_fill(sock, HEADER_LENGTH)
        (packet_len,) = struct.unpack(LENGTH_HEADER, _len)
        data = recv_fill(sock, packet_len)
        header = header_pb2.Header()
        header.ParseFromString(data)
        m = importlib.import_module(header.module)
        clazz = getattr(m, header.clazz)
        obj = clazz()
        func =  getattr(obj, header.method)
        content = recv_fill(sock, header.length)
        ret = func(content)
        if ret == 'quit':
            quit_conn(sock, 'xxx')
        for item in socks:
            print ret
            _len = struct.pack(LENGTH_HEADER, len(ret))
            item.sendall(_len + ret)
        

if __name__ == '__main__':
    server = StreamServer(('0.0.0.0', 8888), recv)
    server.serve_forever()


