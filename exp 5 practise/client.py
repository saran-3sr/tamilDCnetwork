import socket
import threading
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',8000))
def readmsg():
    while True:
        data=s.recv(1024)
        print("server : ",data)
def sendmsg():
    while True:
        msg=input("client : ")
        s.send(msg.encode())
s1=threading.Thread(target=readmsg)
s2=threading.Thread(target=sendmsg)
s1.start()
s2.start()