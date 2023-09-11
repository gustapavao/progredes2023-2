import os

lista_numeros = []
def ordena_bubble(values):
    unsorted_list = values
    for _ in range(len(values)-1): #pq não há ninguém após o último
        for i in range(len(values)-1):
            if values[i] > values[i+1]:
                values[i], values[i+1] = values[i+1], values[i]
    if values != unsorted_list:
        print(True)
        print(values)
    else:
        print(False)
        print(None)

def ordena_selection(values):
    unsorted_list = values
    for i in range(len(values)):
        indice = i
        for d in range(i + 1, len(values)):
            if values[d] < values[indice]:
                indice = d
        (values[i], values[indice]) = (values[indice], values[i])
    if values != unsorted_list:
        print(True)
        print(values)
    else:
        print(False)
        print(None) 

def ordena_insertion(values):
    unsorted_list = values
    for i in range (1, len(values)):
        k = values[i]
        j = i - 1
        while j >= 0 and values[j] > k:
            values[j + 1] = values[j]
            j -= 1
        values[j + 1] = k
    if values != unsorted_list:
        print(True)
        print(values)
    else:
        print(False)
        print(None)     

## PRECISO FAZER UMA FUNÇÃO PARA VERIFICAR SE FOI FEITO O SORTED OU NAO
def ler_arquivo(nome_arquivo):
    try:
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        file_name = diretorio_atual + "/" + nome_arquivo
        opening_file = open(f"{file_name}", "r") 
    except FileNotFoundError:
        print('O arquivo não existe.')
    except:
        print('Houve um erro!')
    else:
        for i in opening_file.readlines():
            try:
                i = (int(i))
            except ValueError:
                print('Ops! Um ou mais dos valores informados não são inteiros.')
            else:
                lista_numeros.append(i)
    finally:
        if len(lista_numeros) != 0:
            print(True)
            print(lista_numeros)
        else:
            print(False)
            print(None)    


def ordena_lista(nome_lista, metodo_ordena):
    pass










ler_arquivo("lista_random.txt")