import socket
import termcolor

IP = "127.0.0.1"
PORT = 8080
MAX_OPEN_REQUESTS = 5

def read_contents(page):
    with open('{}.html'.format(page), 'r') as html_file:
        contents = html_file.read()
    return contents


def process_client(cs):
    """Process the client request.
    Parameters:  cs: socket for communicating with the client"""

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")

    # Print the received message, for debugging
    print()
    print("Request message: ")
    termcolor.cprint(msg, 'green')

    msg = msg.partition('/')          # so we separate the message in three parts: first, GET ; second, / ; third, further instructions
    msg = msg[2].partition(' ')       # now we use partition again so we get the command (/ or /pink or /blue) in the first position

    if msg[0] == '':
        request = 'index'
    elif msg[0] == 'pink':
        request = 'pink'
    elif msg[0] == 'blue':
        request = 'blue'
    else:
        request = 'error'

    contents = read_contents(request)

    # -- Everything is OK
    status_line = "HTTP/1.1 200 OK\r\n"

    # -- Build the header
    header = "Content-Type: text/html\r\n"
    header += "Content-Length: {}\r\n".format(len(str.encode(contents)))

    # -- Build the message by joining together all the parts
    response_msg = str.encode(status_line + header + "\r\n" + contents)
    cs.send(response_msg)

    # Close the socket
    cs.close()


# MAIN PROGRAM

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and PORT
serversocket.bind((IP, PORT))

# Configure the server sockets
# MAX_OPEN_REQUESTS connect requests before refusing outside connections
serversocket.listen(MAX_OPEN_REQUESTS)

print("Socket ready: {}".format(serversocket))

while True:
    # accept connections from outside
    # The server is waiting for connections
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))

    # Service the client
    process_client(clientsocket)
