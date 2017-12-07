import socket
import struct
import sys

#arg 1 : first number
#arg 2 : second number
#arg 3 : operator -- possible operators: + *

values = (int(sys.argv[1]), int(sys.argv[2]), sys.argv[3])
packer = struct.Struct('I I 1s')
packed_data = packer.pack(*values)
	

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost',50)


try:
	sent = client.sendto(packed_data,server_address)
	print "%s bytes sended" % (sent)
	
	data, server = client.recvfrom(4096)
	
	unpacker = struct.Struct('I I')
	unpacked_data = unpacker.unpack(data)
	if unpacked_data[1] == 1:
		print "received from %s : %s" % (server,unpacked_data[0])
	else:
		print "error"
	
finally:
	client.close()