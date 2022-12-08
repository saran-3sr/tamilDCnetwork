import socket
data={
    'google.com':['127.23.23.1','23.231.123.21'],
    'ysyouthgct':'23.1.12.2'
}
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',8000))
s.listen()
conn,addr=s.accept()
with conn:
    ip=conn.recv(1024)
    ip=ip.decode()
    for key,value in data.items():
        if ip in value:
            domain=key
    conn.send(domain.encode())