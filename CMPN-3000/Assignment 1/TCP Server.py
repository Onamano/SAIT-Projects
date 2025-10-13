# Imports
from socket import *

# Declare variables
serverPort = 12000
serverIP = '0.0.0.0'

# Create socket, set time limits, and set socket to listen and accept connections
try:
    # Create and bind socket, print success and details to terminal
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind((serverIP,serverPort))
    print('Server socket created and bound at:', serverIP, "and", serverPort)

    # Set time limit for keeping socket open (20 seconds, before user inputs)
    timeoutSeconds = 20
    serverSocket.settimeout(timeoutSeconds)

    # Set port to listen and provide confirmation to user
    serverSocket.listen(1)
    print('The server is ready to receive')

    # Set socket to accept connections from client
    connectionSocket, addr = serverSocket.accept()

    # Set time limit for keeping socket open (20 seconds, after user inputs)
    timeoutSeconds = 20
    connectionSocket.settimeout(timeoutSeconds)

    # Receive message and echo it back to the client
    try:
        while True:
            sentence = connectionSocket.recv(1024).decode()
            echoedSentence = "Echo from Server: " + sentence
            connectionSocket.send(echoedSentence.encode())
            print("Received from client: " + sentence)
    except TimeoutError:
        print("Socket connection has timed out")
    except:
        serverSocket.close()

except TimeoutError:
    print("Socket connection has timed out")


# References
# Base code outline from J. "F. Kurose and K. W. Ross, Computer networking : a top-down approach. Harlow Pearson, 2021."
# https://stackoverflow.com/questions/42792834/python-continuous-tcp-connection
# https://labex.io/tutorials/python-how-to-implement-error-handling-in-python-socket-communication-398023
