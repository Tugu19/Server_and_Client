import socket

port = 1234
ip = "192.168.56.1"
header = 60

# Create a socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server bins to the ip and port
serverSocket.bind((ip, port))

# Server is listening for a connection for 1 client
serverSocket.listen(1)

print("Server working")

# A new connection from a client
clientSocket, address = serverSocket.accept()

acc = input("Accept the client? > ")

# In case the client is accepted
if acc == "accept":

    # We send to the client that the server accepted it
    clientSocket.send(bytes("accept", "utf-8"))
    print(f"Connection from {address} to the server")

    # Receive the message from the client
    message = clientSocket.recv(header)

    # Disconnect the client from the server
    if message == "<quit>":
        print(f"Client {address} has been disconnected")

    # If the message exist, the server send a response
    elif message:
        print(f'Message: "{message.decode("utf-8")}" received from {address}')
        response = input("Answer: ")
        clientSocket.send(bytes(response, "utf-8"))

# In case the client is denied from the server
elif acc == "decline":
    # Send to the client that he was denied
    clientSocket.send(bytes("false", "utf-8"))
    print(f"Connection from {address} declined")

# Continue the conversation
while True:
    message = clientSocket.recv(header)

    if message == "<quit>":
        print(f"Client {address} has been disconnected")

    elif message:
        print(f'Message: "{message.decode("utf-8")}" received from {address}')
        response = input("Answer: ")
        clientSocket.send(bytes(response, "utf-8"))