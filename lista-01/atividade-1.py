import os.path
import random
#1
while True:
    try:
        quantidade_v = int(input('Informe um número inteiro (quantidade): '))
        valor_minimo_v = int(input('Informe um número inteiro(valor mínimo): '))
        valor_maximo_v = int(input('Informe um número inteiro (valor máximo): '))
    except ValueError:
        print('Ops! O valor informado não é um inteiro.\nInforme os valores de quantidade, valor máximo e valor mínimo novamente:\n\t')
    else:
        break
#2
lista_random = []
def gerar_lista(quantidade, valor_minimo, valor_maximo):
    lista_random.append(valor_maximo)
    lista_random.append(valor_minimo)
    while True:
        lista_random.append(random.randint(valor_minimo, valor_maximo))
        if len(lista_random) == quantidade:
            print('True')
            break
        else: #isso aqui ta errado
            print('False')
            print('None')
            break

gerar_lista(quantidade_v, valor_minimo_v, valor_maximo_v)
#if valor_maximo_v in lista_random:
   # print(lista_random)
#else:
   # pass

#3
def salvar_lista(nome_lista: list, nome_arquivo: str):
    file = open(f'{nome_arquivo}.txt', 'w')
    for i in nome_lista:
        file.write(i+'\n')
    file.close
    file_existence = f'./{nome_arquivo}.txt'
    check_file_existence = os.path.exists(file_existence)
    print(check_file_existence)

    
salvar_lista(lista_random, 'lista random')

    #bool foi gerada?

    #lista or None if false

    #