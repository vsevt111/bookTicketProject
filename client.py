import socket
import clientRegister

port = 5565
s=socket.socket()
s.connect(('192.168.1.37',5565))
message=''
while True:
    data=s.recv(512).decode('utf-8')
    print(data)
    message = input('-> ')
    s.send(message.encode('utf-8'))
s.close()
