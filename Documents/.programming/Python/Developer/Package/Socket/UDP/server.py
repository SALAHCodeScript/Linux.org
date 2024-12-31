import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a local address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

print(f"UDP server is running on {server_address}")

while True:
    # Receive a message from a client
    data, client_address = server_socket.recvfrom(1024)  # Buffer size of 1024 bytes
    print(f"Received message: {data.decode()} from {client_address}")

    # Respond to the client
    response = f"Hello, {client_address}. You said: {data.decode()}"
    server_socket.sendto(response.encode(), client_address)
