import os
import sys
here = (os.path.dirname(__file__))
here = here.replace('view', 'models')
sys.path.append(here)
from gerenciar_arquivos import gerenciar_arquivos


gerenciar_arquivos.descompactar_arquivo()

lista_de_nome = ["ca-2017-01.csv", "ca-2017-02.csv"]#, "ca-2018-01.csv", "ca-2018-02.csv", "ca-2019-01.csv", "ca-2019-02.csv"]
dados = []
for i in range((len(lista_de_nome))):
    dados.append(gerenciar_arquivos.convert_csv_to_list(lista_de_nome[i]))

media_bandeira = gerenciar_arquivos.ajust_bandeira(dados)
media_produto_regiao = gerenciar_arquivos.ajust_regiao(dados)

gerenciar_arquivos.salvar_lista_anp_bandeira(media_bandeira, "media_bandeira")

gerenciar_arquivos.salvar_lista_anp_bandeira(media_produto_regiao, "media_produto_regiao")