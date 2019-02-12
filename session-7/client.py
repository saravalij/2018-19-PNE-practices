
import socket

# First, create the socket. We will always use this parameters: AF_INET y SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Print some information about the socket
print()
print("Socket created:")

PORT = 8080
IP = '212.128.253.64'

s.connect((IP, PORT))

s.send(str.encode("t "))

msg = s.recv(2048).decode('utf-8')

print('Message:' )

print(msg)

s.close()

print('The end')