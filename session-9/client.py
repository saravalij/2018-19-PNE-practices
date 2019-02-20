import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


PORT = 8085
IP = '192.168.1.130'

s.connect((IP, PORT))

s.close()
