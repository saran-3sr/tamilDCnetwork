from concurrent.futures import thread
from pydoc import cli
from string import whitespace
import socket
import time
import threading

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(('127.0.0.1',80))

def getmsg():
  while True:
    msg = client.recv(1000).decode('utf-8')
    print("Server: ",msg)
    time.sleep(0.5)

def sendmsg():
  while True:
    msg = input("")
    # print("\n")

    client.sendall(msg.encode())
    time.sleep(0.5)

thread2 = threading.Thread(target=sendmsg)
thread2.start()

thread1 = threading.Thread(target=getmsg)
thread1.start()
