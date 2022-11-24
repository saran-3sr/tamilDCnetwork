import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',8000))
while True:
    data,addr=s.recvfrom(1024)
    if data.decode()=='exit':
        break
    print(data.decode())
    msg=input("Enter data to send ")
    s.sendto(msg.encode(),addr)
