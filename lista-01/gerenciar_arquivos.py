class gerenciar_arquivos():
    def salvar_lista_em_txt(nome_lista: list, nome_arquivo: str):
        file = open(f'{nome_arquivo}.txt', 'w')
        for i in nome_lista:
            file.writelines(i)
        file.close


    def verificar_existencia_arquivo(nome_arquivo):
        import os
        return os.path.exists(f'./{nome_arquivo}.txt')
    

        