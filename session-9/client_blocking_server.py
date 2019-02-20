
import socket

# SERVER IP, PORT
IP = "192.168.1.130"
PORT = 8086



while True:

    # The client is blocking the server....  NOT A GOOD DESIGN!!! ----> Better if it's there!!!!!!
    msg = input("> ")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # Send the request message to the server
    s.send(str.encode(msg))

    # Receive the servers respoinse
    response = s.recv(2048).decode()

    # Print the server's response
    print("Response: {}".format(response))

    s.close()