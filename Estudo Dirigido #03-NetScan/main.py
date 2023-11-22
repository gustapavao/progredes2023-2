import socket
from utils import Utils

f = open("/home/pavao/ifrn/progredes2023-2/Estudo Dirigido #03-NetScan/portas.txt", "r")
portas = f.readline()
info = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Utils.find()
