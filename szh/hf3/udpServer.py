import socket
import struct

unpacker = struct.Struct('I I 1s')

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_adress = ('localhost', 50)

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
				result = (unpacked_data[0] + unpacked_data[1], 1)
				packer = struct.Struct('I I')
				p_result = packer.pack(*result)
				server.sendto(p_result, client_address)
				print "the resut was sent back"
			elif unpacked_data[2] == '*':
				result = (unpacked_data[0] * unpacked_data[1], 1)
				packer = struct.Struct('I I')
				p_result = packer.pack(*result)
				server.sendto(p_result, client_address)
				print "the resut was sent back"
			else:
				result = (0, 0)
				packer = struct.Struct('I I')
				p_result = packer.pack(*result)
				server.sendto(p_result, client_address)
				print "wrong operator"
	except socket.error, msg:
		print msg

server.close()