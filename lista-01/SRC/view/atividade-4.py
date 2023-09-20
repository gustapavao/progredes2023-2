import os, sys
here = (os.path.dirname(__file__))
here = here.replace('view','models')
sys.path.append(here)
from gerenciar_arquivos import gerenciar_arquivos

lista_de_nome = ["ca-2017-01.csv", "ca-2017-02.csv", "ca-2018-01.csv", "ca-2018-02.csv", "ca-2019-01.csv", "ca-2019-02.csv"]
dados = []
for i in range((len(lista_de_nome))):
    dados.append(gerenciar_arquivos.convert_csv_to_list(lista_de_nome[i]))
lista_completa = list()
for i in dados:
    for k in i:
        lista_completa.append(k)
dados_complementos = list()
