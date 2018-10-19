import socket

s = socket.socket()
s.connect(("127.0.0.1",8080))

ret = str(s.recv(1024),encoding="utf-8")
print(ret)

