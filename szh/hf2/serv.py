import socket
import sys

port = 50
if len(sys.argv) >= 2:
	port = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_addr = ('localhost', port)
s.bind(serv_addr)

s.listen(1)

conn, client_addr = s.accept()

print conn.recv(16)

conn.sendall('Hello client!')


conn.close()