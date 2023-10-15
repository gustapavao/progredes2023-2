import os
import sys
import rarfile


class gerenciar_arquivos():
    
    def salvar_lista_em_txt(nome_lista: list, nome_arquivo: str):
        caminho = sys.argv[0]
        caminho = os.path.split(caminho)
        if ".txt" in nome_arquivo:
            caminho = str(caminho[0] + "/" + f"{nome_arquivo}")
        else:
            caminho = str(caminho[0] + "/" + f"{nome_arquivo}.txt")
        file = open(caminho, 'w')
        for i in nome_lista:
            file.writelines(f'{i}\n')
        file.close()
    
    def verificar_existencia_arquivo(nome_arquivo):
        caminho = sys.argv[0]
        caminho = os.path.split(caminho)
        if ".txt" in nome_arquivo:
            return os.path.exists(caminho[0]+"/"+f"{nome_arquivo}")
        else:
            return os.path.exists(caminho[0]+"/"+f"{nome_arquivo}.txt")
        
    def salvar_lista_anp_bandeira(nome_lista: list, nome_arquivo: str):
        caminho = sys.argv[0]
        caminho = os.path.split(caminho)
        print(caminho)
        caminho = os.path.join(str(caminho[0]),"dados_estatisticos",f"{nome_arquivo}.txt")
        print(caminho)
        file = open(caminho, 'w')
        for i in nome_lista:
            file.writelines(f'{i}\n')
        file.close()
    


    def descompactar_arquivo():
        a = os.path.dirname(__file__)
        a = a.replace("SRC/view", "arquivos_base")
        arq = f"{a}/serie_historica_anp.rar" #ajuste de diretório
        if rarfile.is_rarfile(arq):
            caminho = sys.argv[0]
            caminho = os.path.split(caminho)
            try:
                os.mkdir(os.path.join(caminho[0], "serie_historica_anp"))
                os.mkdir(os.path.join(caminho[0], "dados_estatisticos"))
            except FileExistsError:
                print("\nO arquivo já existe")
                exit()
            file = rarfile.RarFile(arq)
            file.extractall(path=os.path.join(caminho[0], "serie_historica_anp"))
            for f in file.infolist():
                print(f"O arquivo{f.filename} de tamanho {f.file_size} foi extraido com sucesso")

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

    def convert_csv_to_list(nome_arquivo):
        dados =[]
        caminho = sys.argv[0]
        caminho = os.path.split(caminho)
        caminho = os.path.join(caminho[0], "serie_historica_anp/", nome_arquivo)
        files = open(caminho, "r")
        for i in files.readlines():
            i = i.split(";")
            data = i[11]
            data = data.split("/")
            dados.append(
                {
                    "região_sigla": i[0],
                    "estado_sigla": i[1],
                    "Produto": i[10],
                    "Ano": data[-1],
                    "Valor_venda": i[12],
                    "Bandeira": i[15],
                    "Revenda": i[3],
                }
            )
        return dados
    
    def ajust_bandeira(dados):
        media_bandeira = list()
        qtde_postos = []
        valor_venda_total = 0
        divisor = 0
        erro_leitura_valor = 0

        for i in dados:
                for j in i:
                    if j["Revenda"] in qtde_postos:
                        pass
                    else:
                        qtde_postos.append(j["Revenda"])
                    valor = j["Valor_venda"]
                    try:
                        valor = int(valor)
                    except ValueError:
                        erro_leitura_valor += 1
                    else:
                        valor_venda_total += valor
                        divisor += 1

        qtde_postos = set(qtde_postos)

        print("terminou")
        quantidade_de_postos = 0
        for i in range(len(qtde_postos)):
            quantidade_de_postos += i
        print(quantidade_de_postos)

        for i in dados:
            for data in i:
                if data['Produto'] == "Produto":
                    pass
                else:
                    media_bandeira.append({"Bandeira": data["Bandeira"] + "; ", "Produto": data["Produto"] + "; ", "Ano": data["Ano"] + "; ","Valor_médio": f"{valor_venda_total / divisor}; ", "Quantidade_postos": f"{quantidade_de_postos}"})
        return media_bandeira


    def ajust_regiao(dados):
        pass

if __name__ == '__main__':
    gerenciar_arquivos.salvar_lista_anp_bandeira(list())