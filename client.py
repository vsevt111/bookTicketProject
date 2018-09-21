import socket
import clientRegister

port = 5565
s=socket.socket()
s.connect(('localhost',port))
message=''
while True:
    print(s.recv(2048).decode("utf-8"))
    message = input('-> ')
    s.send(message.encode('utf-8'))
s.close()

