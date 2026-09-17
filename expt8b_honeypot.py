import socket
from datetime import datetime
HOST = "0.0.0.0"
PORT = 8888
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)
print("====================================")
print(" SIMPLE PYTHON HONEYPOT")
print("====================================")
print(f"Honeypot started on port {PORT}")
print("Waiting for connections...")
while True:
    client, address = server.accept()
    print("\n[+] Connection Detected")
    print("IP Address :", address[0])
    print("Port :", address[1])
    print("Time :", datetime.now())
    client.send(b"Welcome to Test Server\nEnter a message: ")
    data = client.recv(1024)
    message = data.decode().strip()
    print("Message :", message)
    client.send(b"Message received\n")
    client.close()
    print("[+] Connection Closed")
    print("------------------------------------")
