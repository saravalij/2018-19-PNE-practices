import socket

# SERVER IP, PORT
IP = "192.168.1.130"
PORT = 8087

while True:
    msg = input('Client says: ')

    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    clientsocket.connect((IP, PORT))

    clientsocket.send(str.encode(msg))

    response = clientsocket.recv(2048).decode()

    print("Server responds: {}".format(response))

    clientsocket.close()