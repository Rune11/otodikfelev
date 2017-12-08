import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_adress = ('localhost', 10001)

server.bind(server_adress)

while True:
	try:
		
		data, client_address = server.recvfrom(4096)
		
		print "received %i byte from %s : %s" % (len(data),client_address,data)
		
	except socket.error, msg:
		print msg

server.close()