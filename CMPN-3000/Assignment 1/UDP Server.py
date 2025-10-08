# Imports
from socket import *

# Declare Variables
clientPortUDP = 12000
clientNameUDP = '192.168.1.82'

# Create UDP Socket and bind to port 12000
serverSocketUDP = socket(AF_INET, SOCK_DGRAM)
serverSocketUDP.bind(('', clientPortUDP))

# Set time limit for keeping socket open (20 seconds)
timeoutSeconds = 20
serverSocketUDP.settimeout(timeoutSeconds)

# Confirm server is listening
print('The Server is ready to receive')

try:
    while True:
        # Receive data from client and print to console
        message, clientAddress = serverSocketUDP.recvfrom(2048)
        modifiedMessageUDP = message.decode()
        serverSocketUDP.sendto(modifiedMessageUDP.encode(), clientAddress)
        print("Received from Client: " + modifiedMessageUDP)
        
        # Convert number from string to integer
        if modifiedMessageUDP != "Q":
            numberFromClient = modifiedMessageUDP
            numberFromClient = int(numberFromClient)

        # Calculations
        if modifiedMessageUDP == "Q":
            reply = "Socket connection closed by user"
            print(reply)
            serverSocketUDP.close()
        elif numberFromClient % 2 == 0:
            reply = "Number is even"
            print(reply)
            serverSocketUDP.sendto(reply.encode(), (clientNameUDP, clientPortUDP))
        elif numberFromClient % 2 != 0:
            reply = "Number is odd"
            print(reply)
            serverSocketUDP.sendto(reply.encode(), (clientNameUDP, clientPortUDP))
        else:
            print("Socket connection closed")
            serverSocketUDP.close()
except:
    serverSocketUDP.close()





# References
# https://sqlpey.com/python/solved-top-5-methods-to-set-timeout-on-pythons-socket-recv-method/ - Setting a timeout for the socket
# https://www.programiz.com/python-programming/examples/odd-even - number comparisons