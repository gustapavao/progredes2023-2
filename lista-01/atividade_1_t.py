import random
import os

#a)
while True:
        try:
            valor_1 = int(input('Informe um valor: '))
            valor_2 = int(input('Informe um valor: '))
            valor_3 = int(input('Informe um valor'))
        except ValueError:
            print('Valor errado')
        else:
            break

#b)
lista_random = []
def gerar_lista(a, b, c):
    while True:
        try:
            quantidade = int(a)
            valor_minimo = int(b)
            valor_maximo = int(c)         
        except ValueError:
            print('Valor errado')
        else:
            while True:
                lista_random.append(random.randint(valor_minimo, valor_maximo))
                if len(lista_random) == quantidade:
                    print(True)
                    return(lista_random)  
        finally:
            if len(lista_random) == quantidade:
                print(lista_random)
                return True
            else:
                print(None)
                return False
                




def salvar_lista(nome_lista, nome_arquivo):
    file = open(f'{nome_arquivo}.txt', 'w')
    for i in nome_lista:
        file.writelines(f'{i}\n')
    file.close()
    print(os.path.exists(f'./{nome_arquivo}.txt'))


print(gerar_lista(1000,1,100000))
salvar_lista(lista_random, 'exercicio1')