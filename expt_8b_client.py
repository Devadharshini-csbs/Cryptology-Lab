import socket
HOST = "127.0.0.1"
PORT = 8888
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
message = client.recv(1024)
print(message.decode())
user_message = input("Type Message: ")
client.send(user_message.encode())
response = client.recv(1024)
print(response.decode())
client.close()
