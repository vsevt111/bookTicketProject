import socket
import clientRegister

port = 12002
s=socket.socket()
s.connect(("192.168.1.3",port))
print('Welcome press any button to start')
message=''
while True:
    message = input('-> ')
    s.send(message.encode('utf-8'))
    data=s.recv(1024).decode('utf-8')
    print(data)
s.close()