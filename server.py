# -*- coding: utf-8 -*-

from gevent.server import StreamServer
import struct
import traceback
import message_pb2
import player_pb2

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
    (peer_ip, peer_port) = sock.getpeername()
    while True:
        _len = recv_fill(sock, HEADER_LENGTH)
        (packet_len,) = struct.unpack(LENGTH_HEADER, _len)
        data = recv_fill(sock, packet_len)
        if data is None:
            quit_conn(sock, 'xxx')
            break
        msg = _len + data
        tt = message_pb2.Message()
        tt.ParseFromString(data)
        print tt.content
        if tt.content == 'quit':
            print tt.player.name
            quit_conn(sock, tt.player.name)
            break
        for item in socks:
            # (_ip, _port) = item.getpeername()
            # if _ip == peer_ip and _port == peer_port:
            #    continue
            item.sendall(msg)      

if __name__ == '__main__':
    server = StreamServer(('0.0.0.0', 8888), recv)
    server.serve_forever()





