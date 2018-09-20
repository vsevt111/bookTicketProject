import socket
import clientRegister

<<<<<<< HEAD
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
=======
while(True):
    clientSocket = socket(AF_INET,SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    sentence = input("Input lowercase sentence:")
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    print("From Server:", modifiedSentence.decode())
    clientSocket.close()
>>>>>>> master
