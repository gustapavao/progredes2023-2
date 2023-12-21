import socket
from utils_nets import Utils
from netscan import NetScan

file = open('progredes2023-2\Estudo Dirigido #03-NetScan\portas.txt', 'r')
for i in file.readlines():
    i = i.split('/')
    port = i[0]
    protocol = Utils.verify_protocol(i[1])
    protocol_name = Utils.protocol_name(i[1])
    result = NetScan(port=port, protocol=protocol)
    if result == "Closed":
        pass
    elif result == "Open":
        pass
    else:
        pass

# Porta NNN : Protocolo: PPPP (TCP ou UDP): (DDDD)/ STATUS: YYYY(Responde ou Não Responde)