import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost',10000)
message = "Ez lesz az uzenet amit kuldunk"

try:
	sent = client.sendto(message,server_address)
	print "%s bytes sended" % (sent)
	
	data, server = client.recvfrom(4096)
	print "received from %s : %s" % (server,data)
	
finally:
	client.close()