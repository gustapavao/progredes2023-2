from random import randint
from os import path
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
        lista_random.append(valor_minimo)
        lista_random.append(valor_maximo)
        while True:
            lista_random.append(randint(valor_minimo, valor_maximo))
            if len(lista_random) == quantidade:
                print(True)
                print(lista_random)
                break
                


gerar_lista(quantidade_v, valor_minimo_v, valor_maximo_v)
if len(lista_random) != quantidade_v:
    print(False)
    print(None)



def salvar_lista(nome_lista: list, nome_arquivo: str):
    file = open(f'{nome_arquivo}.txt', 'w')
    for i in nome_lista:
        file.writelines(f'{i}\n')
    file.close
    file_existence = f'./{nome_arquivo}.txt'
    check_file_existence = path.exists(file_existence)
    print(check_file_existence)

    
salvar_lista(lista_random, 'lista_random')

