import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',8000))
while True:
    message=input("Enter the data ")
    s.sendall(message.encode())
    data=s.recv(1024)
    print(data)