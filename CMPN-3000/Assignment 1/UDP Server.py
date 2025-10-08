# Imports
from socket import *

# Declare Variables
clientPort = 12000
clientIP = '192.168.1.82'

# Create UDP Socket and bind to port 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', clientPort))

# Set time limit for keeping socket open (20 seconds)
timeoutSeconds = 20
serverSocket.settimeout(timeoutSeconds)

# Confirm server is listening
print('The Server is ready to receive')

try:
    while True:
        # Receive data from client and print to console, size is 2048 bytes
        message, clientAddress = serverSocket.recvfrom(2048)
        modifiedMessage = message.decode()
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)
        print("Received from Client: " + modifiedMessage)
        
        # Convert number from string to integer
        if modifiedMessage != "Q":
            numberFromClient = modifiedMessage
            numberFromClient = int(numberFromClient)

        # Calculations
        if modifiedMessage == "Q":
            reply = "Socket connection closed by user"
            print(reply)
            serverSocket.close()
        elif numberFromClient % 2 == 0:
            reply = "Number is even"
            print(reply)
            serverSocket.sendto(reply.encode(), (clientIP, clientPort))
            modifiedReply, serverAddressUDP = serverSocket.recvfrom(2048)
        elif numberFromClient % 2 != 0:
            reply = "Number is odd"
            print(reply)
            serverSocket.sendto(reply.encode(), (clientIP, clientPort))
            modifiedReply, serverAddressUDP = serverSocket.recvfrom(2048)
        else:
            print("Socket connection closed")
            serverSocket.close()
except:
    serverSocket.close()





# References
# https://sqlpey.com/python/solved-top-5-methods-to-set-timeout-on-pythons-socket-recv-method/ - Setting a timeout for the socket
# https://www.programiz.com/python-programming/examples/odd-even - number comparisons