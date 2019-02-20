import socket
import termcolor

PORT = 8087
IP = "192.168.1.130"
MAX_OPEN_REQUESTS = 5


def process_client(cs):
    """Process the client request.
    Parameters:  cs: socket for communicating with the client"""

    msg = cs.recv(2048).decode("utf-8")

    if msg.upper() == 'EXIT':
        exit()
    else:
        print("Request message: {}".format(msg))
        cs.send(str.encode(termcolor.colored(msg, 'blue')))
        cs.close()

# MAIN PROGRAM

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

serversocket.listen(MAX_OPEN_REQUESTS)

print("Socket ready: {}".format(serversocket))

while True:

    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    print("Attending connections from client: {}".format(address))

    # Service the client# Configure the Server's IP and PORT
    process_client(clientsocket)