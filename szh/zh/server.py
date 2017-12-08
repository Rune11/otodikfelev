import socket
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

server_address = ('localhost',10000)
server.bind(server_address)

store = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
store_address = ('localhost',10001)

server.listen(5)

inputs = [server]

outputs = []


while inputs:
	timeout = 1
	readable, writeable, exceptional = select.select(inputs, outputs, inputs, timeout)
	
	if not (readable or writeable or exceptional):
		continue
	
	for s in readable:
		if s is server:
			client, client_address = s.accept()
			client.setblocking(1)
			print "new connection from ", client_address			
			inputs.append(client)
			outputs.append(client)
		else:
			data = s.recv(4096)
			#g,q = data.split(' ')
			
			store.sendto(data, store_address)
			
#	for s in exceptional