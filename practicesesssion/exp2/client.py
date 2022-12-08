import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    data=input("Enter the data to send: ")
    s.sendto(str.encode(data),('127.0.0.1',8000))