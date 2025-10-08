# Imports
from socket import *

# Declare variables
serverPort = 12000
serverIP = '0.0.0.0'

# create and bind socket
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverIP,serverPort))

# Set time limit for keeping socket open (20 seconds)
timeoutSeconds = 20
serverSocket.settimeout(timeoutSeconds)

# Set port to listen and provide confirmation to user
serverSocket.listen(1)
print('The server is ready to receive')

# Receive message and echo it back to the client
try:
    while True:
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(1024).decode()
        capitalizedSentence = "Echo from Server: " + sentence
        connectionSocket.send(capitalizedSentence.encode())
        # connectionSocket.close()
        print("Received from client: " + sentence)
except:
    serverSocket.close()