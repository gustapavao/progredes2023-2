import os, sys, json
here = (os.path.dirname(__file__))
here = here.replace('view','models')
sys.path.append(here)

# Carregue o arquivo JSON
with open("/home/pavao/Desktop/Estudos/arquivos/dados_cartola_fc/cartola_fc_2021.txt", "r", encoding="utf-8") as file:
    data = json.load(file)