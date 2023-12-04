import socket
import threading

nickname = input("Nickname: ")

HOST = '127.0.0.1'
PORT = 55555
CODE = 'utf-8'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            message = client.recv(1024).decode(CODE)
            if message == 'NICK':
                client.send(nickname.encode(CODE))
            else:
                print(message)
        except:
            print("An error ocurred!")
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode(CODE))

receive_thread= threading.Thread(target=write)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()