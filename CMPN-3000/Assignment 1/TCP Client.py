# Imports
from socket import *

# Connection Variables
serverIP = '192.168.1.78'
serverPort = 12000

# Socket Connection
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP,serverPort))

# Input & Send
sentence = input('Input lowercase sentence: ')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)

# Server Verification Message was Sent and Capitalized
print('From Server: ', modifiedSentence.decode())

# Close Socket
clientSocket.close()