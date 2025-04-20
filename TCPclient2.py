from socket import *

serverName = "127.0.0.1"
serverPort = 1200

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

sentence = input("Input lowercase sentence: ")
clientSocket.send(sentence.encode())

modifiedSentence = clientSocket.recv(1024).decode()
print("From Server:", modifiedSentence)

clientSocket.close()