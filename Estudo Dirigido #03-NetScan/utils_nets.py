import socket

class Utils:
    def verify_protocol(protocol:str):
        try:
            protocol = protocol.split('\t')
            if protocol[0] == "TCP,UDP":
                return "TCP/UDP"
            elif protocol[0] == "TCP":
                return "TCP"
            elif protocol[0] == "UDP":
                return "UDP"
        except IndexError:
            print('aqui foi')
    def protocol_name(protocol:str):
        try:
            protocol = protocol.split('\t')
            protocol = protocol[1]
            return protocol
        except:
            return "ERRO"


