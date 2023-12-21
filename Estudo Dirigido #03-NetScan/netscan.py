import socket


class NetScan:
    SOCKETS = {
        "TCP": socket.socket(socket.AF_INET, socket.SOCK_STREAM),
        "UDP": socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    } 
    HOST = "127.0.0.1"

    def __init__(self, port, protocol):
        socket_protocol = self.protocol_socket(protocol=protocol)
        c = self.connect_socket(port= port, protocol_param=socket_protocol)
        return c
        



    def protocol_socket(self, protocol):
        if protocol == "TCP":
            return self.SOCKETS["TCP"]
        elif protocol == "UDP":
            return self.SOCKETS["UDP"]
        elif protocol == "TCP/UDP":
            return ((self.SOCKETS["TCP"]), self.SOCKETS["UDP"])

    def connect_socket(self, protocol_param, port):
        try:
            if len(protocol_param) == 2:
                print("TCP/UDP CALMA PAPAI")
        except TypeError:
            sock = protocol_param
            try:
                result = sock.connect_ex((self.HOST, int(port)))
            except AttributeError:
                print (f'Houve um erro ao tentar conectar na porta {port}')
            else:
                if result == 0:
                    sock.close()
                    return "Open"
                else:
                    sock.close()
                    return "Closed"