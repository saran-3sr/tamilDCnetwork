import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',8000))
while True:
    data=s.recv(1024)
    print(data)