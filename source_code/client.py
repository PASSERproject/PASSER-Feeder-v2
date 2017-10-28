#!/usr/bin/python
import socket               # Import socket module

# Andrew Ray
# Radford University

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

result="ok"
s.connect((host, port))
data=3
data = bytes(data, 'UTF-8')
s.send(data)
s.close()
