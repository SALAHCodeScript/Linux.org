#!/usr/bin/python3
import socket

def handle_client(client_socket):
    # Receive the client's request (e.g., GET / HTTP/1.1)
    request = client_socket.recv(1024).decode()
    print(f"Received request:\n{request}")

    # Prepare a simple HTTP response
    response = "HTTP/1.1 200 OK\r\n"
    response += "Content-Type: text/html\r\n\r\n"
    response += "<html><body><h1>Hello, World!</h1></body></html>"

    # Send the response
    client_socket.send(response.encode())
    client_socket.close()

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to an address and port
server_socket.bind(('localhost', 8080))

# Listen for incoming connections
server_socket.listen(5)
print("HTTP Server listening on port 8080...")

while True:
    # Accept a client connection
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    # Handle the client request
    handle_client(client_socket)
