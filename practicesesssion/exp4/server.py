import socket
from datetime import datetime as time
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',8000))
s.listen()
conn,addr=s.accept()
with conn:
    while True:
        data=time.now().time()
        print(data)
        data=data.strftime("%m/%d/%Y, %H:%M:%S")
        conn.sendall(data.encode('UTF-8'))
        
