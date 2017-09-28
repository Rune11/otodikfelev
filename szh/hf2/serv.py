import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_addr = ('localhost', 50)
s.bind(serv_addr)

s.listen(1)

conn, client_addr = s.accept()

print conn.recv(16)

conn.sendall('Hello client!')


conn.close()