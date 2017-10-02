import socket               # Import socket module

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)         # Create a socket object
port = 12346                # Reserve a port for your service.


while True:
	a=raw_input()
	s.sendto(a,("127.0.0.1",12346))
	recv=s.recvfrom(100)
	print recv[0]


