import socket
import sys

port = 50
if len(sys.argv) >= 2:
	port = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', port)
s.connect(server_address)
s.send("Hello Server")
print s.recv(16)
s.close()

