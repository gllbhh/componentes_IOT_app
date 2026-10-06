import socket

HOST = "127.0.0.1"  # replace with the server's IP address when testing across two hosts
PORT = 65432
MESSAGE = "Hello from the TCP client!"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    client_socket.sendall(MESSAGE.encode("ascii"))
    print(f"Sent: {MESSAGE}")
