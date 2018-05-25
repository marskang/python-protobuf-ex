# -*- coding: utf-8 -*-

from gevent.server import StreamServer
import person_pb2

sockets = list()

def echo(_socket, address):
    # print('New connection from %s:%s' % address)
    #sockets.append(_socket)
    #sockname =  _socket.getpeername()
    #ip = sockname[0]
    #port = sockname[1]
    #while True:
        #buff = _socket.recv(1024)
        #for s in sockets:
        #    peer_ip = s.getpeername()[0]
        #    peer_port = s.getpeername()[1]
        #    print peer_ip, peer_port, ip, port
    per = person_pb2.person()
    per.id = 6
    per.name = 'zjk'
    data = per.SerializeToString()
    _socket.send(data)
            
            # if peer_ip == ip and peer_port == port:
            #    continue
            #s.send(buff)
            

if __name__ == '__main__':
    server = StreamServer(('0.0.0.0', 8888), echo)
    server.serve_forever()


