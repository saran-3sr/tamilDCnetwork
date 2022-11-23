import socket
from datetime import datetime as time
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',8000))
s.listen()
conn,addr=s.accept()
with conn:
    date=time.now().time()
    print(date)
    date=date.strftime("%m/%d/%Y, %H:%M:%S")
    encodedata=date.encode('UTF-8')
    conn.sendall(encodedata)