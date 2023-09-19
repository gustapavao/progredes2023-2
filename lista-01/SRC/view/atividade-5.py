import os
import sys

here = (os.path.dirname(__file__))
here = here.replace('view', 'models')
sys.path.append(here)

from gestor_cartola import Cartola

campeonato_ano = input("Você gostaria de utilizar o Brasileirão de 2021 ou 2022 para montar seu time? ")
anos_disponiveis = ["2021", "2022"]
if campeonato_ano in anos_disponiveis:
    pass
else:
    print("Você escolheu um ano que não está disponível no momento")
    exit()

while True:
    try:
        formacao = int(input("Escolha uma das formações a seguir:\n\t1 para 3-4-3\n\t2 para 3-5-2\n\t3 para 4-3-3\n\t4 para 4-4-2\n\t5 para 4-5-1\n\t6 para 5-3-2\n\t7 para 5-4-1\n\t\tSUA FORMAÇÃO:"))
    except ValueError:
        print('Você precisa escolher uma das opções')
    else:
        if formacao <= 0:
            print("Opção inválida!")
            exit()
        opcoes = [1, 2, 3, 4, 5, 6, 7]
        if formacao in opcoes:
            break
        else:
            print('Você precisa escolher uma das opções\n\n')

Cartola(forma_time=formacao, ano=campeonato_ano)
