
import socket

PORT = 8088
IP = '192.168.1.132'


clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((IP, PORT))

request = 'h\nPERCA\nCOMPLEMENT\nlen\nsup'

clientsocket.send(str.encode(request))

response = clientsocket.recv(2048).decode('utf-8')

print()
print(response)

clientsocket.close()
