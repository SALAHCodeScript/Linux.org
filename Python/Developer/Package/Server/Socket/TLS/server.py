#!/usr/bin/python3
import socket
import ssl

# Paths to the key and certificate files
key_file = "keyfile.pem"
cert_file = "certfile.pem"

# Create an SSL context
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile=cert_file, keyfile=key_file)

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)

print("Secure server listening on port 12345...")

while True:
    # Accept a new connection
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    # Wrap the connection with SSL
    with context.wrap_socket(client_socket, server_side=True) as secure_socket:
        secure_socket.send(b"Hello, secure world!")
