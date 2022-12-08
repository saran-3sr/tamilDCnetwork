import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msg=input("Hi enter a welcome messsage to activate server : ")
s.sendto(str.encode(msg),('127.0.0.1',8000))
while True:
    data,addr=s.recvfrom(1024)
    print("-> ",data)
    msg=input("Enter the data ")
    s.sendto(str.encode(msg),addr)