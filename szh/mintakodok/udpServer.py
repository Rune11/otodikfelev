import socket
import struct

unpacker = struct.Struct('I I 1s')

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_adress = ('localhost', 10000)

server.bind(server_adress)
server.settimeout(1.0)

while True:
	try:
		print "waiting..."
		data, client_address = server.recvfrom(4096)
		
		unpacked_data = unpacker.unpack(data)
		
		print "received %i byte from %s : %s" % (len(data),client_address,unpacked_data)
		
		if unpacked_data:
			if unpacked_data[2] == '+':
				result = unpacked_data[0] + unpacked_data[1]
				result = htons(result)
				server.sendto(result, cleint_address)
				print "the resut was sended back"
			elif unpacked_data[2] == '*':
				result = unpacked_data[0] * unpacked_data[1]
				result = htons(result)
				server.sendto(result, cleint_address)
				print "the resut was sended back"
	except socket.error, msg:
		print msg

server.close()