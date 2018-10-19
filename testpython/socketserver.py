
import socket

sk = socket.socket()
sk.bind(("127.0.0.1",8080))
sk.listen(5)
i = 1
conn,address = sk.accept()
conn.sendall(bytes("Hello world",encoding="utf-8"))

