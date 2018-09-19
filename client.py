from socket import*
serverName = input("insert server name")
serverPort = int(input("insert port number"))

while(True):
    clientSocket = socket(AF,SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    sentence = input ("Input lowercase sentence:")
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    print("From Server:",modifiedSentence.decode())
    clientSocket.close()