# -*- coding: utf-8 -*-

import socket
from pb import message_pb2
import player_pb2
import struct
from pb import header_pb2

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

msg = message_pb2.Message()
player = msg.player
player.id = 1
player.name = '张三'
msg.content = '大家好才是真的好的'

content = msg.SerializeToString()

header = header_pb2.Header()
header.length = len(content)
header.module = 'msg_req'
header.clazz = 'MsgReq'
header.method = 'test'

_str = header.SerializeToString()
packet_len = struct.pack(LENGTH_HEADER, len(_str))
s.sendall(packet_len + _str)
s.sendall(content)
s.close()

