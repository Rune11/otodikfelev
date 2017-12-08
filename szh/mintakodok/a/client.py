import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address=('localhost',10000)
message = raw_input('Mit kugyek?')
print message

client.connect(server_address)

try:
	
	client.sendall(message)
	
	data = client.recv(4096)
	print "received: %s" % data
finally:
	client.close()