# -*- coding: utf-8 -*-

import socket
import message_pb2
import player_pb2
import struct
import threading
import time
import os

HOST = '127.0.0.1'
PORT = 8888
LENGTH_HEADER = '!I'

HEADER_LENGTH = struct.calcsize(LENGTH_HEADER)

all_msg = ''


class RecvThread(threading.Thread):
    
    def __init__(self, sock):
        super(RecvThread, self).__init__()
        self.sock = sock

    def run(self):
        while True:
            global all_msg
            _len = recv_fill(self.sock, HEADER_LENGTH)
            (packet_len,) = struct.unpack(LENGTH_HEADER, _len)
            data = recv_fill(s, packet_len)
            msg = message_pb2.Message()
            msg.ParseFromString(data)
            os.system('clear')
            t = '\n' + msg.player.name + ': ' + msg.content + '\n'
            all_msg +=  t
            print all_msg
            print 'input content:'


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
name = raw_input('input name:')
id = raw_input('input id:')
recv_thread = RecvThread(s)
recv_thread.start()
while True:
    content = raw_input('\ninput content:\n')
    msg = message_pb2.Message()
    player = msg.player
    player.id = int(id)
    player.name = name
    msg.content = content
    data = msg.SerializeToString()
    packet_len = struct.pack(LENGTH_HEADER, len(data))
    s.sendall(packet_len + data)







