import sys,os
here = (os.path.dirname(__file__))
here = here.replace('view','models')
sys.path.append(here)


from random import randint
from gerenciar_arquivos import gerenciar_arquivos

while True:
    try:
        quantidade_v = int(input('Informe um número inteiro (quantidade): '))
        valor_minimo_v = int(input('Informe um número inteiro(valor mínimo): '))
        valor_maximo_v = int(input('Informe um número inteiro (valor máximo): '))
    except ValueError:
        print('Ops! O valor informado não é um inteiro.\nInforme os valores de quantidade, valor máximo e valor mínimo novamente:\n\t')
    else:
        break

lista_random = []
def gerar_lista(quantidade, valor_minimo, valor_maximo):
    try:
        quantidade = int(quantidade)
        valor_minimo = int(valor_minimo)
        valor_maximo = int(valor_maximo)
    except:
        print('Ops! O valor informado não é um inteiro.\nInforme os valores novamente:')
    else:
        while True:
            lista_random.append(randint(valor_minimo, valor_maximo))
            if len(lista_random) == quantidade:
                break

gerar_lista(quantidade_v, valor_minimo_v, valor_maximo_v)
gerenciar_arquivos.salvar_lista_em_txt(lista_random, "lista_random")          

if gerenciar_arquivos.verificar_existencia_arquivo("lista_random"):
    print(True)
else:
    print(False)