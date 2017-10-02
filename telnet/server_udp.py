#!/usr/bin/python           # This is server.py file

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

##############################   Validating for USER EXISTANCE   ##########################


if uname=="root":
        os.chdir("/root/")
elif uname!="root":
	filesearch=commands.getstatusoutput("cat /etc/passwd | grep -w  {}".format(uname))
	if filesearch[0]==0:
		msg_user="Successfully logged in  !!!"
        	homedir=commands.getstatusoutput("   ls /home/ | grep -w  {}    ".format(uname))
		s.sendto(msg_user,data[1])

##############################   Validating for USER DIRECTORY EXISTANCE   ##########################

		if homedir[0]==0:
			os.chdir("/home/{}".format(uname))
			dirmsg="[{}@station169 ~]".format(uname)
			s.sendto(dirmsg,data[1]) 
	

			while True:
        			cmd=s.recvfrom(100)
        			print cmd[0]
        			if '|' in cmd[0]:
        			        output=subprocess.check_output(cmd[0], shell=True)
        			        s.sendto(output.rstrip(),data[1])
        			else:
        			        a=commands.getstatusoutput(cmd[0])
        			        aa=a[1]
        			        s.sendto(aa,data[1])






		else:
			msg_dir= " Home directory /home/{} does not exist. Sending you to /temp".format(uname)
			os.chdir("/temp")
			s.sendto(msg_dir,data[1])

##############################   NOT LOGGING IN ##########################

else:
	msg="Wrong creds. Try logging in again !!"
	s.sendto(msg,data[1])

