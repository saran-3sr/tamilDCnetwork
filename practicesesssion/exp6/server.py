import socket
import threading

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',8000))
s.listen(1)
conn,addr=s.accept()

print("Connection Accepted ")

def getMsg():
    while True:
        msg=conn.recv(1024)
        print("Server -> ",msg.decode())
def recMsg():
    while True:
        msg=input(" ")
        conn.send(msg.encode())
thread1=threading.Thread(target=getMsg)
thread2=threading.Thread(target=recMsg)
thread1.start()
thread2.start()