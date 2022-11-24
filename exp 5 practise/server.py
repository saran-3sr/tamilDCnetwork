import socket
import threading
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',8000))
s.listen()
conn,addr=s.accept()
def readmsg():
    while True:
        data=conn.recv(1024)
        print("\nClient : ",data)
def sendmsg():
    while True:
        msg=input("Server : ")
        conn.send(msg.encode())
s1=threading.Thread(target=readmsg)
s2=threading.Thread(target=sendmsg)
s1.start()
s2.start()

