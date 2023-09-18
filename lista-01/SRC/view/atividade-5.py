import os, sys, json

here = (os.path.dirname(__file__))
here = here.replace('view','models')
sys.path.append(here)

from gestor_cartola import Cartola


escolha = input("De qual ano? ")
formacao = int(input("Escolha uma das formações a seguir:\n\t1 para 3-4-3\n\t2 para 3-5-2\n\t3 para 4-3-3\n\t4 para 4-4-2\n\t5 para 4-5-1\n\t6 para 5-3-2\n\t7 para 5-4-1\n\t\tSUA FORMAÇÃO:"))



if escolha == "2021":
    with open("/home/pavao/Desktop/Estudos/arquivos/dados_cartola_fc/cartola_fc_2021.txt", "r", encoding="utf-8") as file:
        data = json.load(file)
        file.close()
elif escolha == "2022":
    with open("/home/pavao/Desktop/Estudos/arquivos/dados_cartola_fc/cartola_fc_2022.txt", "r", encoding="utf-8") as file:
        data = json.load(file)
        file.close()
else:
    print("Você escolheu um ano que não está disponível no momento")
    exit()



Cartola(data, forma_time =formacao)
