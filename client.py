# -*- coding: utf-8 -*-

import socket
import person_pb2

HOST = '127.0.0.1'
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = s.recv(1024)
target = person_pb2.person()
target.ParseFromString(data)
print(target.id)
print(target.name)
s.close()

