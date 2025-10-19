# Imports
from socket import *

# Create socket, set time limits, and set socket to listen and accept connections
def serverSetup(serverPort, serverIP):
    try:
        # Create and bind socket, print success and details to terminal
        serverSocket = socket(AF_INET,SOCK_STREAM)
        serverSocket.bind((serverIP,serverPort))
        print("Server socket created and bound at:", serverIP, "and", serverPort)

        # Set time limit for keeping socket open (20 seconds, before user inputs)
        timeoutSeconds = 20
        serverSocket.settimeout(timeoutSeconds)

        # Set port to listen and print confirmation to terminal
        serverSocket.listen(1)
        print("The server is ready to receive")

        #Accept client connection
        connectionSocket, addr = serverSocket.accept()
        print("Connected with:", addr)

        # Set time limit for keeping connection open
        timeoutSeconds = 20
        connectionSocket.settimeout(timeoutSeconds)
        
        #Receive and echo message back to client 
        while True:
            sentence = connectionSocket.recv(1024).decode()
            echoedSentence = "Echo from Server: " + sentence
            connectionSocket.send(echoedSentence.encode())
            print("Received from client: " + sentence)
    
    except TimeoutError:
        print("Socket connection has timed out")

    except ConnectionAbortedError:
        print("Connection closed by client")

    finally:
        connectionSocket.close()

if __name__ == "__main__":
    serverPort = 12000
    serverIP = '0.0.0.0'
    serverSetup(serverPort, serverIP)

# References
# Base code outline from J. "F. Kurose and K. W. Ross, Computer networking : a top-down approach. Harlow Pearson, 2021."
# https://stackoverflow.com/questions/42792834/python-continuous-tcp-connection
# https://labex.io/tutorials/python-how-to-implement-error-handling-in-python-socket-communication-398023
# https://realpython.com/python-sockets
