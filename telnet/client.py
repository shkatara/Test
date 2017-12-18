#!/usr/bin/python           

import socket               # Import socket module

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)         # Create a socket object
port = 12346                # Reserve a port for your service.



user=raw_input("shubham login: ")
s.sendto(user,("127.0.0.1",12346))
passwd=raw_input("Password: ")
s.sendto(passwd,("127.0.0.1",12346))
 
while True:
        cmd=raw_input("[{}@localhost ~]$ ".format(user))
	s.sendto(cmd,("127.0.0.1",12346))
	result=s.recvfrom(10000)[0]
	print result
	#print "\n{}@127.0.0.1 ~]$ {}".format(user,result)
