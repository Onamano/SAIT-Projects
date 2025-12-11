# Imports
from socket import *
from ssl import *

def clientSetup(serverName, serverPort, sentence):
    try:
        # Define context for TLS
        context = SSLContext(PROTOCOL_TLS_CLIENT)

        # For use with self-signed certificate
        context.check_hostname = False
        context.verify_mode = CERT_NONE

        # Create client socket
        clientSocket = socket(AF_INET, SOCK_STREAM)

        # Wrap client socket with TLS context
        tlsSocket = context.wrap_socket(clientSocket, server_hostname=serverName)

        try:
            # Connect to server
            tlsSocket.connect((serverName,serverPort))
            print('Connected to:', serverName, 'and', serverPort)

            # Input message & send to server
            try:
                while True:
                    sentence = input('Input sentence (Q to quit): ')
                    if sentence == 'Q':
                        sentence = 'Client has disconnected'
                        tlsSocket.send(sentence.encode())
                        break
                    if len(sentence) == 0:
                        print('Please enter a message with a length greater than 0')
                        break
                    tlsSocket.send(sentence.encode())
                    echoedSentence = tlsSocket.recv(1024)

                    # Print the echoed message for the client
                    print(echoedSentence.decode())
            except TimeoutError:
                print('Socket connection has timed out')
            except:
                tlsSocket.close()

        except TimeoutError:
            print('Socket connection has timed out')

        except ConnectionRefusedError:
            print('Unable to connect to server')

    except OSError:
        print('Unable to create client socket')

    #Ensures the socket is closed
    finally:
        tlsSocket.close()

if __name__ == "__main__":
    serverName = '127.0.0.1'
    serverPort = 12000
    sentence = ''
    clientSetup(serverName, serverPort, sentence)

# References
# Base code outline from J. "F. Kurose and K. W. Ross, Computer networking : a top-down approach. Harlow Pearson, 2021."
# Code adapted from previous Project 1 code.
# https://stackoverflow.com/questions/42792834/python-continuous-tcp-connection
# https://labex.io/tutorials/python-how-to-implement-error-handling-in-python-socket-communication-398023
# https://realpython.com/python-sockets
