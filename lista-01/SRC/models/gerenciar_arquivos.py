class gerenciar_arquivos():
    def salvar_lista_em_txt(nome_lista: list, nome_arquivo: str):
        file = open(f'{nome_arquivo}.txt', 'w')
        for i in nome_lista:
            file.writelines(f'{i}\n')
        file.close


    def verificar_existencia_arquivo(nome_arquivo):
        import os
        return os.path.exists(f'./{nome_arquivo}')
    
    # def verificar_existencia_arquivo_neste_diretorio(nome_arquivo):
    #     import os
    #     __dir_atual = os.path.dirname(os.path.abspath(__file__))
    #     return os.path.exists(f'{__dir_atual}/{nome_arquivo}')
    
    def ler_arquivo_inteiros(nome_arquivo):
        lst_valores = None
        try:
            arquivo = open(nome_arquivo, 'r')
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
        
