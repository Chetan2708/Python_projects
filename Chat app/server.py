from socket import *
from threading import *

# Set to store connected clientsx``
clients = set()

def clientThread(clientSocket, clientAddress):
    try:
        while True:
            # Receive the message from the client
            message = clientSocket.recv(1024).decode("utf-8")
            
            # Check if the message is empty
            if not message:
                raise Exception("Empty message received")  # Raise an exception for empty messages
                
            # Display the message and broadcast to other clients
            print(clientAddress[0] + ":" + str(clientAddress[1]) + " says: " + message)

            for client in clients:
                if client is not clientSocket:
                    client.send((clientAddress[0] + ":" + str(clientAddress[1]) + " says: " + message).encode("utf-8"))


    except Exception as e:
        print(f"Error in client thread: {e}")

    finally:
        # Remove the client from the set and close the socket
        clients.remove(clientSocket)
        print(clientAddress[0] + ":" + str(clientAddress[1]) + " disconnected")
        clientSocket.close()

def main():
    try:
        # Set up the server socket
        hostSocket = socket(AF_INET, SOCK_STREAM)
        hostSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

        # Set the server's IP address and port number
        hostIp = "127.0.0.1"
        portNumber = 7500
        
        # Bind the socket to the specified address and port
        hostSocket.bind((hostIp, portNumber))
        hostSocket.listen()
        print("Waiting for connection...")

        while True:
            # Accept incoming client connection
            clientSocket, clientAddress = hostSocket.accept()
            
            # Add the client socket to the set of connected clients
            clients.add(clientSocket)
            print("Connection established with: ", clientAddress[0] + ":" + str(clientAddress[1]))

            # Send a new user connected message to all clients
            new_user_message = f"New user connected from {clientAddress[0]}:{clientAddress[1]}"
            for client in clients:
                try:
                    client.send(new_user_message.encode("utf-8"))
                except Exception as e:
                    print(f"Error sending new user message to {client}: {e}")

            # Create a new thread for the client
            thread = Thread(target=clientThread, args=(clientSocket, clientAddress,))
            thread.start()

    except Exception as e:
        print(f"Error in main server loop: {e}")
    finally:
        # Close the server socket
        hostSocket.close()

if __name__ == "__main__":
    # Start the main function when the script is executed
    main()
