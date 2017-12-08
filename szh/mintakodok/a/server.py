import socket
import select

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
server_address = ('localhost', 10000)
server.bind(server_address)

logger = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
log_address = ('localhost',10001)

inputs = [server]

outputs = []


server.listen(5)
timeout = 1

while(inputs):
	readable, writeable, exceptional = select.select(inputs, outputs, inputs, timeout)
	
	if not (readable or writeable or exceptional):
		continue
	
	for s in readable:
		if s is server:
			client, client_address = s.accept()
			client.setblocking(1)
			inputs.append(client)
			outputs.append(client)
		else:
			data = s.recv(4096)
			a,b,m=data.split(' ')
			lhs = int(a)
			rhs = int(b)
			valasz = 0
			if m == '+':
				valasz = lhs+rhs
			elif m == '-':
				valasz = lhs-rhs
			elif m == '*':
				valasz = lhs*rhs
			elif m == '/':
				valasz = lhs/rhs
			
			s.sendall(str(valasz))
			
			logger.sendto(str(valasz),log_address)
			
			print "client close"
			if s in outputs:
				outputs.remove(s)
			inputs.remove(s)
			s.close()
			if s in writeable:
				writeable.remove(s)
	
	

		#a,b,c = [int(x) for x in data.split(' ')]

server.close()
		