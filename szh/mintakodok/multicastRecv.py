import socket
import struct

multicast_group = '224.3.29.71'
server_address = ('',10000)

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(server_address)
server.settimeout(1.0)


group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
server.setsockopt(socket.IPPROTO_IP,socket.IP_ADD_MEMBERSHIP, mreq)

while True:
	try:
		data, address = server.recvfrom(1024)
		print "received from %s : %s" % (address, data)

		server.sendto('ack',address)
		print "ack sended"
	except socket.error, msg:
		print msg
server.close()