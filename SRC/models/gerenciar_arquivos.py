import os, dpkt
class gerenciar_arquivos():
    
    def salvar_lista_em_txt(nome_lista: list, nome_arquivo: str):
        diretorio_salvar = os.path.dirname(__file__)
        diretorio_salvar = os.path.split(diretorio_salvar)
        diretorio_salvar = os.path.join(diretorio_salvar[0], "view", f'{nome_arquivo}.txt')
        print(diretorio_salvar)
        file = open(diretorio_salvar, 'w')
        for i in nome_lista:
            file.writelines(f'{i}\n')
        file.close


    def verificar_existencia_arquivo(nome_arquivo):
        diretorio_salvar = os.path.dirname(__file__)
        diretorio_salvar = os.path.split(diretorio_salvar)
        return os.path.exists(os.path.join(diretorio_salvar[0], "view", f'{nome_arquivo}.txt'))

    def ler_arquivo_inteiros(nome_arquivo):
        lst_valores = None
        diretorio_verificar = os.path.dirname(__file__)
        diretorio_verificar = os.path.split(diretorio_verificar)
        diretorio_verificar = os.path.join(diretorio_verificar[0], "view", f'{nome_arquivo}.txt')
        try:
            arquivo = open(diretorio_verificar, 'r')
        except:
            ('Houve um erro.')
        else:
            lst_valores = list()
            while True:
                f = arquivo.readlines()
                if not f: break
                for i in f:
                    try:
                        lst_valores.append(int(i))
                    except ValueError:
                        print('Houve um erro com um ou mais valores do arquivo')
                arquivo.close()
        finally:
            return lst_valores
        
    def process_tcpdump_file(filename):
        with open(filename, 'rb') as file:
            pcap = dpkt.pcap.Reader(file)
            for timestamp, buf in pcap:
                eth = dpkt.ethernet.Ethernet(buf)

            
                if isinstance(eth.data, dpkt.ip.IP):
                    ip = eth.data

                # Extract source and destination IP addresses
                    src_ip = dpkt.utils.inet_to_str(ip.src)
                    dst_ip = dpkt.utils.inet_to_str(ip.dst)

                print(f"Timestamp: {timestamp}, Source IP: {src_ip}, Destination IP: {dst_ip}")

if __name__ == '__main__':
    gerenciar_arquivos.salvar_lista_em_txt(list(), 'test')