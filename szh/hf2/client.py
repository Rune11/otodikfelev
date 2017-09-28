import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 50)
s.connect(server_address)
s.send("Hello Server")
print s.recv(16)
s.close()

