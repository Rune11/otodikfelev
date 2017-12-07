import socket
import struct
import select
import Queue
import sys
import pickle

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

server_address = ('localhost',10000)
server.bind(server_address)

server.listen(5)

inputs = [server]

outputs = []

def add(list1, list2):
	for i in range(0,len(list1)):
		for j in range(0,len(list2)):
			list1[i][j] += list2[i][j]
	return list1
		
zajForAll = False
Chipcodes = {
	'A' : (1,1,1,1),
	'B' : (1,-1,1,-1),
	'C' : (1,1,-1,-1),
	'D' : (1,-1,-1,1)
}
# --- TODO: hozz letre egy valtozot, ami tarolni fogja az aktualis uzenetet, pl zaj
zaj = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] #4es tupleokbol allo lista
#zaj kikuldese: dataToSend = pickle.dumps(zaj) 
#zaj fogadasa (client) : Data = server.recv(4096)   zaj = pickle.loads(Data)
chipcodes = {}

while inputs:
	timeout = 1
	readable, writeable, exceptional = select.select(inputs, outputs, inputs, timeout)
	
	if not (readable or writeable or exceptional):
		continue
	
	for s in readable:
		if s is server:
			client, client_address = s.accept()
			client.setblocking(1)
			name = client.recv(20)
			print "new connection from ", client_address,"with azon", name
			packer = struct.Struct('i i i i')
			if name == "A" :
				packedData = packer.pack(Chipcodes['A'][0],Chipcodes['A'][1],Chipcodes['A'][2],Chipcodes['A'][3])
				client.send(packedData)
			if name == "B" :
				packedData = packer.pack(Chipcodes['B'][0],Chipcodes['B'][1],Chipcodes['B'][2],Chipcodes['B'][3])
				client.send(packedData)
			if name == "C" :
				packedData = packer.pack(Chipcodes['C'][0],Chipcodes['C'][1],Chipcodes['C'][2],Chipcodes['C'][3])
				client.send(packedData)
			if name == "D" :
				packedData = packer.pack(Chipcodes['D'][0],Chipcodes['D'][1],Chipcodes['D'][2],Chipcodes['D'][3])
				client.send(packedData)
			# --- TODO: Modositsd az alabbi kodot, hogy a kliens uzenete alapjan valszold meg neki a chipkodjat
			# --- TODO: pl: kliens elkuldte A kuld vissza neki hogy 1111
			
			inputs.append(client)
			outputs.append(client)
		elif not sys.stdin.isatty():
		# elif s == sys.stdin
			print "Close the system"
			inputs.remove(server)
			for c in inputs:
				inputs.remove(c)
				c.close()
			server.close()
			inputs = []
		else:
			data = s.recv(1024)
			data = data.strip()
			if data:
				print "received data: ",data,"from",s.getpeername()
				packer = struct.Struct('i i i i')
				if data == 'B':
					packedData = packer.pack(Chipcodes['B'][0],Chipcodes['B'][1],Chipcodes['B'][2],Chipcodes['B'][3])
					client.send(packedData)
				elif data == 'A':
					packedData = packer.pack(Chipcodes['A'][0],Chipcodes['A'][1],Chipcodes['A'][2],Chipcodes['A'][3])
					client.send(packedData)
				elif data == 'C':
					packedData = packer.pack(Chipcodes['C'][0],Chipcodes['C'][1],Chipcodes['C'][2],Chipcodes['C'][3])
					client.send(packedData)
				elif data == 'D':
					packedData = packer.pack(Chipcodes['D'][0],Chipcodes['D'][1],Chipcodes['D'][2],Chipcodes['D'][3])
					client.send(packedData)
				else :
					
					code = pickle.loads(data)
					zaj = add(zaj,code)
					zajForAll = True
				# A readable client socket has data
				# --- TODO: kezeld a klienstol kapott uzenetet:
				# --- TODO: ha kliens egy chipkodot kert, akkor valszold meg neki
				# --- TODO: ha uzenet jott, akkor add hozza a ZAJhoz, majd jelezd hogy el kell kuldeni mindenkinek

			else:
				print "client close"
				if s in outputs:
					outputs.remove(s)
				inputs.remove(s)
				s.close()
				if s in writeable:
					writeable.remove(s)

	# --- TODO: ha kaptal uzenetet, akkor kuld el mindenkinek
		if zajForAll : 
			dataToSend = pickle.dumps(zaj)
			for s in writeable:
				s.send(dataToSend)
			zajForAll = False	
			# next_msg = ""
			# print "sending:",next_msg,"to",s.getpeername()
			# s.send(next_msg)
		
		
		
		
		
		
		
		
		
		
		
		
		