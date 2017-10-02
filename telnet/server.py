#!/usr/bin/python           # This is server.py file

import socket,commands               # Import socket and commands module

s = socket.socket()         # Create a socket object

ip="127.0.0.1"
port = 12346             # Reserve a port for your service.
s.bind((ip, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
    
   c,addr = s.accept()     # Establish connection with client.
   c.send('''Trying 192.168.1.150...
Connected to 192.168.1.150.
Escape character is ^]
\n
Kernel 3.10.0-123.13.2.el7.x86_64 on an x86_64
''')   
   user=c.recv(100)
   passwd=c.recv(100)
   print user
   print passwd
   c.send('''\n[root@127.0.0.1 ~]$ ''')
