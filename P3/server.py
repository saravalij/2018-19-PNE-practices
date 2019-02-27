import socket
from P1.Seq import Seq

PORT = 8088
IP = "192.168.1.132"
MAX_OPEN_REQUESTS = 5

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def command_processing(obj, com):
    com = com.lower()
    try:
        if com.startswith('perc'):
            return str(obj.perc(com[4].upper()))
        elif com.startswith('count'):
            return str(obj.count(com[5].upper()))
        elif com == 'len':
            return str(obj.len())
        elif com == 'complement':
            return obj.complement().strbase
        elif com == 'reverse':
            return obj.reverse().strbase
        else:
            return 'ERROR'
    except IndexError:
        return 'Error'


def process_client(cs):

    request = cs.recv(2048).decode("utf-8")
    print('Request: {}'.format(request))
    print()

    request = request.split('\n')

    if request[0] == '':
        response = 'ALIVE'
    elif all(x in ['A', 'C', 'G', 'T'] for x in request[0].upper()) == False:
        response = 'ERROR'
    else:
        response = ['OK']
        sequence = Seq(request[0].upper())
        for c in request[1:]:
            response.append(command_processing(sequence, c))
        response = '\n'.join(response)

    cs.send(str.encode(response))
    cs.close()

    print()


try:
    serversocket.bind((IP, PORT))

    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = serversocket.accept()

        print("Attending connections from client: {}".format(address))

        process_client(clientsocket)

except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()
