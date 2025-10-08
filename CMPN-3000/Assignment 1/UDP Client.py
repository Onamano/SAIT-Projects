# Imports
from socket import *

# Declare Variables
serverIP = '192.168.1.78'                                       # IP Address for the UDP server
serverPortUDP = 12000                                           # Port number for socket connection
message = ''                                                    # Placeholder for user input variable

# Create socket
clientSocketUDP = socket(AF_INET, SOCK_DGRAM)

# Sending data to the server with error handling
try:
    while message != "Q":
        userMessage = input("Enter a number (Q to exit): ")
        clientSocketUDP.sendto(userMessage.encode(), (serverIP, serverPortUDP))
        modifiedMessage, serverAddressUDP = clientSocketUDP.recvfrom(2048)
        message = userMessage
except:
    clientSocketUDP.close()