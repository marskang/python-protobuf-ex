# -*- coding: utf-8 -*-

from gevent.server import StreamServer
import struct
import message_pb2
import player_pb2

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

socks = list()


def recv(sock, addr):
    
    socks.append(sock)
    (peer_ip, peer_port) = sock.getpeername()
    while True:
        _len = recv_fill(sock, HEADER_LENGTH)
        (packet_len,) = struct.unpack(LENGTH_HEADER, _len)
        data = recv_fill(sock, packet_len)
        msg = _len + data
        tt = message_pb2.Message()
        tt.ParseFromString(data)
        print tt.content
        for item in socks:
            # (_ip, _port) = item.getpeername()
            # if _ip == peer_ip and _port == peer_port:
            #    continue
            item.sendall(msg)      

if __name__ == '__main__':
    server = StreamServer(('0.0.0.0', 8888), recv)
    server.serve_forever()





