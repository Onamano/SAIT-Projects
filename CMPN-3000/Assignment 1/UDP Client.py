# Imports
from socket import *

# Declare Variables
serverIP = '192.168.1.78'                                       # IP Address for the UDP server
serverPort = 12000                                              # Port number for socket connection
message = ''                                                    # Placeholder for user input variable

# Create socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Sending data to the server with error handling
try:
    while message != "Q":
        userMessage = input("Enter a number (Q to exit): ")
        clientSocket.sendto(userMessage.encode(), (serverIP, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        message = userMessage
        
        # Receive data from client and print to console, size is 2048 bytes
        reply, clientAddress = clientSocket.recvfrom(2048)
        modifiedReply = reply.decode()
        print("Received from Server: " + modifiedReply)
except:
    clientSocket.close()