#!/usr/bin/python3
import socket
import ssl

# Path to the certificate file (CA or server cert)
cert_file = "certfile.pem"

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Wrap the socket with SSL
secure_socket = ssl.wrap_socket(
    client_socket,
    cert_reqs=ssl.CERT_REQUIRED,
    ca_certs=cert_file
)

# Connect to the secure server
secure_socket.connect(('localhost', 12345))
print(secure_socket.recv(1024).decode())
secure_socket.close()
