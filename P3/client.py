
import socket
import pickle

PORT = 8080
IP = '192.168.1.133'

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((IP, PORT))

print("TIP: Whenever client's ready to send the introduced requests, just type in 'send'.\n")

requests = []
req = input('> ')
req = req.upper()

if req == '':
    requests.append(req + 'SEND')
else:
    if all(x in ['A', 'C', 'G', 'T'] for x in req) == True:
        requests.append(req)
    else:
        requests.append('ERROR' + 'SEND')

while requests[-1] != 'SEND':
    req = input('> ')
    req = req.upper()
    requests.append(req)


for c in requests:
    message = pickle.dumps(requests)
    clientsocket.send(message)


response = clientsocket.recv(2048).decode(pickle.loads(recvd_message))     #recv(2048).decode('utf-8')
print(response)
clientsocket.close()
