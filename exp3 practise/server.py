import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',8000))
print("Server up and listing")
s.listen()
conn,addr=s.accept()
with conn:
    data=conn.recv(1024)
    if not data:
        print("No data received")
    else:
        print(data)
        conn.sendall(data)