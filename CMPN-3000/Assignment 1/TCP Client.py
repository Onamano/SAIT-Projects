# Imports
from socket import *

# Connection Variables
serverName = '192.168.50.38'
serverPort = 12000
sentence = ''

try:
    # Create client socket
    clientSocket = socket(AF_INET, SOCK_STREAM)

    # Set time limit for keeping socket open (20 seconds, does not currently work due to clientSocket.connect blocking the timeout)
    timeoutSeconds = 20
    clientSocket.settimeout(timeoutSeconds)

    try:
        # Connect to server
        clientSocket.connect((serverName,serverPort))
        print('Connected to:', serverName, 'and', serverPort)

        # Input message & send to server
        try:
            while True:
                sentence = input('Input sentence (Q to quit): ')
                if sentence == 'Q':
                    sentence = 'Client has disconnected'
                    clientSocket.send(sentence.encode())
                    break
                if len(sentence) == 0:
                    print('Please enter a message with a length greater than 0')
                    break
                clientSocket.send(sentence.encode())
                echoedSentence = clientSocket.recv(1024)

                # Print the echoed message for the client
                print(echoedSentence.decode())
        except TimeoutError:
            print('Socket connection has timed out')
        except:
            clientSocket.close()

    except TimeoutError:
        print('Socket connection has timed out')

    except ConnectionRefusedError:
        print('Unable to connect to server')

except OSError:
    print('Unable to create client socket')

finally:
    clientSocket.close()

# References
# Base code outline from J. "F. Kurose and K. W. Ross, Computer networking : a top-down approach. Harlow Pearson, 2021."
# https://stackoverflow.com/questions/42792834/python-continuous-tcp-connection
# https://labex.io/tutorials/python-how-to-implement-error-handling-in-python-socket-communication-398023
