import socket

host = '127.0.0.1'
port = 50002

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

def send_command(message):
    if message != "":
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        if message.startswith("ip"):
            print("IPv4 and IPv6 addresses:")
            print(data)
        else:
            print("Response from server: " + str(data))

message = input(">> ")

while message != "exit":
    if message.startswith("get"):
        # Dosya isteği yaparken sunucuya dosya adını bildirin
        client_socket.send(message.encode())
        file_data = client_socket.recv(1024).decode()
        print("File content:\n" + file_data)
    else:
        send_command(message)
    message = input(">> ")

client_socket.close()
