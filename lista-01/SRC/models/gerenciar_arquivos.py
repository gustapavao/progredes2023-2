import os
import dpkt
import sys
import rarfile


class gerenciar_arquivos():
    
    def salvar_lista_em_txt(nome_lista: list, nome_arquivo: str):
        caminho = sys.argv[0]
        caminho = os.path.split(caminho)
        caminho = str(caminho[0] + "/" + f"{nome_arquivo}.txt")
        
        file = open(caminho, 'w')
        for i in nome_lista:
            file.writelines(f'{i}\n')
        file.close()

    def descompactar_arquivo():
        arq = "/home/pavao/Desktop/Estudos/arquivos/serie_historica_anp.rar"
        if rarfile.is_rarfile(arq):
            caminho = sys.argv[0]
            caminho = os.path.split(caminho)
            try:
                os.mkdir(os.path.join(caminho[0], "serie_historica_anp"))
            except FileExistsError:
                print("\nThe directory already exists")
                exit()
            file = rarfile.RarFile(arq)
            file.extractall(path=os.path.join(caminho[0], "serie_historica_anp"))
            for f in file.infolist():
                print(f"O arquivo{f.filename} de tamanho {f.file_size} foi extraido com sucesso")

    def verificar_existencia_arquivo(nome_arquivo):
        caminho = sys.argv[0]
        caminho = os.path.split(caminho)
        return os.path.exists(caminho[0]+"/"+f"{nome_arquivo}.txt")

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

    def convert_csv_to_list_save(nome_arquivo):
        dados =[]
        caminho = sys.argv[0]
        caminho = os.path.split(caminho)
        caminho = os.path.join(caminho[0], "serie_historica_anp/", nome_arquivo)
        files = open(caminho, "r")
        for i in files.readlines():
            i = i.split(";")
            dados.append(
                {
                    "região_sigla": i[0],
                    "estado_sigla": i[1],
                    #"municipio": i[2],
                    #"Revenda": i[3],
                    #"CPNJ_revenda": i[4],
                    #"Nome_rua": i[5],
                    #"Numero_rua": i[6],
                    #"Complemento": i[7],
                    #"Bairro": i[8],
                    #"CEP": i[9],
                    "Produto": i[10],
                    "Data_coleta": i[11],
                    "Valor_venda": i[12],
                    #"Valor_compra": i[13],
                    #"Unidade_medida": i[14],
                    "Bandeira": i[15],

                }
            )
        return dados
    def convert_csv_to_list(nome_arquivo):
        dados =[]
        caminho = sys.argv[0]
        caminho = os.path.split(caminho)
        caminho = os.path.join(caminho[0], "serie_historica_anp/", nome_arquivo)
        files = open(caminho, "r")
        for i in files.readlines():
            i = i.split(";")
            dados.append(
                {
                    "região_sigla": i[0],
                    "estado_sigla": i[1],
                    #"municipio": i[2],
                    #"Revenda": i[3],
                    #"CPNJ_revenda": i[4],
                    #"Nome_rua": i[5],
                    #"Numero_rua": i[6],
                    #"Complemento": i[7],
                    #"Bairro": i[8],
                    #"CEP": i[9],
                    "Produto": i[10],
                    "Data_coleta": i[11],
                    "Valor_venda": i[12],
                    "Valor_compra": i[13],
                    "Unidade_medida": i[14],
                    "Bandeira": i[15],

                }
            )
        return dados
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