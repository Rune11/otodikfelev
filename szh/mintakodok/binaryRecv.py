import socket
import struct

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

server_address = ('localhost',10000)
server.bind(server_address)
server.listen(1)
server.settimeout(1.0)

unpacker = struct.Struct('I 2s f')

while True:
	try:
		client, address = server.accept()
		client.setblocking(1)
		try:
			data = client.recv(unpacker.size)
			print "received: %s" % data
			
			unpacked_data = unpacker.unpack(data)
			print "unpacked",unpacked_data
		finally:
			client.close()
	except socket.error, msg:
		print msg
server.close()