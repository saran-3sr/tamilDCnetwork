import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',8000))
while True:
    data,addr=s.recvfrom(1024)
    print("->",data)
    msg=input('Enter the data to send : ')
    s.sendto(str.encode(msg),addr)
    

    