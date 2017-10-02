#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)         # Create a socket object
port = 12346                # Reserve a port for your service.



user=raw_input("shubham login: ")
s.sendto(user,("127.0.0.1",12346))
passwd=raw_input("Password: ")
s.sendto(passwd,("127.0.0.1",12346))
auth=s.recvfrom(1000)
print auth[0]
dirauth=s.recvfrom(1000)
print dirauth[0]
 
while True:
        cmd=raw_input("[{}@station169 ~]$ ".format(user))
	s.sendto(cmd,("127.0.0.1",12346))
	result=s.recvfrom(10000)[0]
	print result
	#print "\n{}@127.0.0.1 ~]$ {}".format(user,result)
