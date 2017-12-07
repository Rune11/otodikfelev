import socket
import struct

message = "ez az uzenet mindenkinek"
multi_group = ('224.3.29.71',10000)

sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sender.settimeout(1.0)

ttl = struct.pack('b',1)
sender.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL,ttl)

try:
	sent = sender.sendto(message, multi_group)
	print "msg sended"
	
	while True:
		print "waiting.."
		try:
			data, address = sender.recvfrom(16)
			print "received from %s : %s " % (address, data)
		except:
			print "timeout"
			break
finally:
	sender.close()
		