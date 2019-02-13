import socket

from P1.Seq import Seq


PORT = 8082  # teacher: 8080
IP = '212.128.253.109'  # teacher: 212.128.253.64

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sequence = Seq(input('Introduce a sequence: '))
    s.connect((IP, PORT))
    s.send(str.encode('\n> Complement sequence: ' + sequence.complement().strbase + '\n> Reversed sequence: ' + sequence.reverse().strbase))
    msg = s.recv(2048).decode('utf-8')
    print('Message:' )
    print(msg)
    s.close()

print('Finished.')
