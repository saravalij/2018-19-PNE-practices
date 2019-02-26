
import socket

PORT = 8082
IP = '212.128.253.102'


clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

requests = []

while True:
    req = input('> ')
    requests.append(red)

    if len(requests) == 0:
        print('h')
        break
    else:



    if
    clientsocket.connect((IP, PORT))
    clientsocket.send(str.encode(message))
    req = clientsocket.recv(2048).decode('utf-8')
    print('Message:' )
    print(req)
    clientsocket.close()
