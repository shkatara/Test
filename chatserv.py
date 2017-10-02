#!/usr/bin/python           # This is server.py file

import socket,commands,os               # Import socket and commands module

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)         # Create a socket object

ip="0.0.0.0"
port = 12346             # Reserve a port for your service.
s.bind((ip, port))        # Bind to the port

while True:
	a=s.recvfrom(100)
	print a[0]
    b=raw_input()
	s.sendto(b,a[1])

