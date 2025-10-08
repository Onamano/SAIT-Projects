# Imports
from socket import *

# Connection Variables
serverName = '192.168.1.78'
serverPort = 12000
sentence = ''

# Socket Connection
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

# Set time limit for keeping socket open (20 seconds)
timeoutSeconds = 5
clientSocket.settimeout(timeoutSeconds)

# Input message & send to server
try:
    while sentence != "Q":
        sentence = input('Input sentence (Q to quit): ')
        clientSocket.send(sentence.encode())
        modifiedSentence = clientSocket.recv(1024)

        # Server Verification Message was Sent and Capitalized
        print(modifiedSentence.decode())
except:
    clientSocket.close()