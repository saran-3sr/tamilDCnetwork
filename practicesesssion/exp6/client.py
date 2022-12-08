import socket
import threading

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',8000))

def getmsg():
    while True:
        msg=s.recv(1024)
        print("Server-> ",msg)
def sendMsg():
    while True:
        msg=input("Client-> ")
        s.send(msg.encode())
thread1=threading.Thread(target=getmsg)
thread2=threading.Thread(target=sendMsg)
thread1.start()
thread2.start()