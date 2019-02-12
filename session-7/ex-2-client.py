

import socket

# First, create the socket. We will always use this parameters: AF_INET y SOCK_STREAM


PORT = 8082  # teacher: 8080
IP = '212.128.253.102'  # teacher: 212.128.253.64

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    message = input('What do you want to say?: ')
    s.connect((IP, PORT))
    s.send(str.encode(message))
    msg = s.recv(2048).decode('utf-8')
    print('Message:' )
    print(msg)
    s.close()

print('The end')