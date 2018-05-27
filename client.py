# -*- coding: utf-8 -*-

import socket
import message_pb2
import player_pb2
import struct

HOST = '127.0.0.1'
PORT = 8888
LENGTH_HEADER = '!I'

HEADER_LENGTH = struct.calcsize(LENGTH_HEADER)

def recv_fill(sock, packet_len):
    buff = ''
    while len(buff) < packet_len:
        data = sock.recv(packet_len - len(buff))
        if not data:
            return
        buff += data
    return buff


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

_len = recv_fill(s, HEADER_LENGTH)
(packet_len,) = struct.unpack(LENGTH_HEADER, _len)
data = recv_fill(s, packet_len)
msg = message_pb2.Message()
msg.ParseFromString(data)
print msg.content
print msg.player.id
print msg.player.name
s.close()


