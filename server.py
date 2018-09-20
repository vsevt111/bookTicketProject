from clientRegister import clientRegister
from socket import*
p = clientRegister()
serverPort = int(input("insert port number"))
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("THE server is ready for receive")
while(True):
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    print(capitalizedSentence)
    connectionSocket.close()