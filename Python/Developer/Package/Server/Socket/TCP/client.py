#!/usr/bin/python3.13
import socket

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(('localhost', 12345))

# Send some data
client_socket.sendall(b"Hello, Server!")

# Receive the response
response = client_socket.recv(1024)
print(f"Received: {response.decode()}")

# Close the connection
client_socket.close()
