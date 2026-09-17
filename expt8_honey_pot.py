import socket
from datetime import datetime

HOST = "0.0.0.0"
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print("Honeypot started on port", PORT)

while True:
    client, address = server.accept()

    print("\n[+] Connection Detected")
    print("IP Address :", address[0])
    print("Port :", address[1])
    print("Time :", datetime.now())

    client.send(b"Welcome to Server\n")
    client.close()
