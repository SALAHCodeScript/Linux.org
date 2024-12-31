#!/usr/bin/python3
import socket

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ipv4_address = socket.gethostbyname(hostname)

# Bind the socket to an address and port
server_socket.bind((ipv4_address, 12345))

# Listen for incoming connections (5 is the backlog size)
server_socket.listen(5)
print("Server is listening...")

# Accept an incoming connection
client_socket, addr = server_socket.accept()
print(f"Connected by {addr}")

# Receive data (max buffer size is 1024 bytes)
data = client_socket.recv(1024)
print(f"Received: {data.decode()}")

# Send a response
client_socket.sendall(b"Hello, Client!")

# Close the connection
client_socket.close()
server_socket.close()
