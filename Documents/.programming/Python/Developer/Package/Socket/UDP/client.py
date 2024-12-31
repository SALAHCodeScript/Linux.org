#!/usr/bin/python3
import socket

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address
server_address = ('localhost', 12345)

try:
    # Send a message to the server
    message = "Hello, Server!"
    client_socket.sendto(message.encode(), server_address)
    print(f"Sent message to server: {message}")

    # Receive a response from the server
    response, server = client_socket.recvfrom(1024)
    print(f"Received response from server: {response.decode()}")
finally:
    # Close the socket
    client_socket.close()
