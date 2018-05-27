# -*- coding: utf-8 -*-

from gevent.server import StreamServer
import struct
import message_pb2
import player_pb2

LENGTH_HEADER = '!I'


def recv(sock, addr):
    msg = message_pb2.Message()
    player = msg.player
    player.id = 1
    player.name = '张三'
    msg.content = 'hello world'
    data = msg.SerializeToString()
    packet_len = struct.pack(LENGTH_HEADER, len(data))
    sock.sendall(packet_len + data)          

if __name__ == '__main__':
    server = StreamServer(('0.0.0.0', 8888), recv)
    server.serve_forever()





