import socket
from P1.Seq import Seq
import pickle


# Configure the Server's IP and PORT

PORT = 8080
IP = "192.168.1.133"
MAX_OPEN_REQUESTS = 5

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    serversocket.bind((IP, PORT))

    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        # accept connections from outside
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = serversocket.accept()

        print("Attending connections from client: {}".format(address))

        message = serversocket.recv(2048).decode(pickle.loads(recvd_message))     #recv(2048).decode("utf-8")
        serversocket.send(pickle.dumps(x for x in message))
        serversocket.close()

        #if req == ''

        #response = Seq(req).complement()
        #send_bytes = str.encode(response.strbase)

        #clientsocket.send(send_bytes)
        #clientsocket.close()

except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()




