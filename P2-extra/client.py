import socket

from P1.Seq import Seq


PORT = 8094  # teacher: 8080
IP = '212.128.253.109'  # teacher: 212.128.253.64

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sequence = input('Introduce a sequence: ')
    s.connect((IP, PORT))
    s.send(str.encode(sequence))
    msg = s.recv(2048).decode('utf-8')
    print('> Complement sequence:', msg)
    s.close()

print('Finished.')
