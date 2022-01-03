import socket
import sys

header = 60
ok = 1

# Choose the ip and the port
while ok:
    ip = input("select the server ip address >  ")
    port = int(input("select the server port > "))
    ok = 0

    # In case the ip is wrong, type again
    if ip != "192.168.56.1":
        print("Incorrect IP. Try again")
        ok = 1

# Create a socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to a server running at a certain ip and port
clientSocket.connect((ip, port))

# In case the server is not accepting the client, he receive a denial parameter from the server
data = clientSocket.recv(header)
if data.decode("utf-8") == "false":
    print("Connection declined")
    sys.exit()

# Exit condition
print('To exit the server type: "<quit>"')

while True:
    message = input("Write a message: ")
    # If the message is "<quit>" the client disconnect from the server
    if message == "<quit>":
        clientSocket.send(bytes("<quit>", "utf-8"))
        print("You have been disconnected")
        sys.exit()

    # Client sent the message to the server
    clientSocket.send(bytes(message, "utf-8"))
    # Client receive the message from the server
    answer = clientSocket.recv(header)
    print(f"Server: {answer.decode('utf-8')}")