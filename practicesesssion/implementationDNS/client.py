import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',8000))
ip =input("Enter the ip address ")
s.send(ip.encode())
domain=s.recv(1024)
print("Domain ",domain)