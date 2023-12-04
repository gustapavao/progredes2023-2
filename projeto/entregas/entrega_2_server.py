import threading
import socket

HOST = '127.0.0.1'
PORT = 55555
CODE = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat!'.encode(CODE))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send('NICK'.encode(CODE))
        nickname = client.recv(1024).decode(CODE)
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}')
        broadcast (f'{nickname} joined the chat'.encode(CODE))
        client.send('Connected to the server!'.encode(CODE))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("SERVER is listening")
receive()