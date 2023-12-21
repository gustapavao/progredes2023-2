import socket

SOCKETS = {
        "TCP": socket.socket(socket.AF_INET, socket.SOCK_STREAM),
        "UDP": socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    } 

print(len(SOCKETS["TCP"]))