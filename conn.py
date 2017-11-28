import socket, sys

port = 80
try:
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	print("socket was created successfully")
except socket.error:
	print("socket wasn't created successfully")

hip = socket.gethostbyname("www.fb.com")

try:
	s.connect((hip,port))
	print("\nwe are connected to %s on port %s" %(hip,port))
except socket.gaierror:
	print("\nconnection failed!!")


