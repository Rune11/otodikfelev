import socket
import sys
import struct
import time
import select
import msvcrt
import pickle

username = sys.argv[1]

# --- TODO: implementald a dekodolo fv-t, ami egy jelsorozatbol es a sajat chipkod alapajan lekerdezi a neki szant uzenetet
def decode_bit(bit):
	if bit>0:
		return 1
	elif bit<0:
		return 0
	else: 
		return 0

def matmul(A,B):
	nA = len(A)
	mB = len(B[0])
	j = len(A[0])
	res = [ [ 0 for i in range(mB)] for k in range(nA) ]
	for i in range(nA):
		for k in range(mB):
			for x in range(j):
				res[i][k] += A[i][x]*B[x][k]
	return res

def decode_message(noise, rck):
	col_chip = [ [i] for i in rck ]
	decoded = matmul(noise,col_chip)
	normed = [ decode_bit(a[0]) for a in decoded ]
	return normed

# --- TODO: implementald a kodolo fv-t, ami egy adott chipkod alapjan elkesziti a kodolt uzenetet
def encode_bit(bit,chip):
	if bit=='1':
		return chip
	else:
		return [ -1*i for i in chip ]
		
def encode_message(message,chip):
	to_send = [ encode_bit(i,chip) for i in message ]
	return to_send

def prompt(nl):
	if nl:
		print ''
	sys.stdout.write('<'+username+'> ')
	sys.stdout.flush()

def readInput(timeout = 1):
	start_time = time.time()
	input = ''
	while True:
		if msvcrt.kbhit():
			chr = msvcrt.getche()
			if ord(chr) == 13:	#enter
				break
			elif ord(chr) >= 32: #space_char
				input += chr
		if len(input) == 0 and ((time.time() + start_time) > timeout):
			break
	
	if len(input) > 0:
		return input
	else:
		return ''
	
server_address = ('localhost',10000)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(server_address)
client.settimeout(1.0)


client.send(username)
unpacker = struct.Struct('i i i i')
UnpackedChipkod = client.recv(4096)
Chipkod = unpacker.unpack(UnpackedChipkod)
recivedChipkod = []
print Chipkod

prompt(False)

while True:
	socket_list = [client]
	
	readable, writable, error = select.select(socket_list, [],[],1)
	
	for s in readable:
		data = client.recv(4096)
		if not data:
			print "disconnect"
			client.close()
			sys.exit()
		else:
			code = pickle.loads(data)
			uzi = decode_message(code, list(Chipkod))
			if uzi==[0,0,0,0] : 
				print "nem kaptal semmit :("
			else:
				print uzi
			# --- TODO: kodold vissza a kapott zajbol hogy kaptal-e uzenetet, majd irasd ki, azt is ha nincs uzenet
				
	try:
		msg = readInput()
		if msg != '':
			client.send(msg[0])
			UnpackedChipkod = client.recv(4096)
			recivedChipkod = unpacker.unpack(UnpackedChipkod)
			mess = msg[2:]
			#print (encode_message(mess,recivedChipkod))
			dataToSend = pickle.dumps(encode_message(mess,list(recivedChipkod)))
			client.send(dataToSend)
		# --- TODO: a beolvasott uzenet alapjan kerd le a szervertol a megfelelo chipkodot
		# --- TODO: a kapott chipkod alapjan kodold msg-ben tallahato uzenetet majd kuld el a szervernek
		
	except socket.error, msg:
		print msg

client.close()

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	