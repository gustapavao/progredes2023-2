lista_numeros = []
def ordena_bubble():
    pass

def ler_arquivo(nome_arquivo):
    try:
        opening_file = open(f"{nome_arquivo}", "r") 
    except FileNotFoundError:
        print('O arquivo não existe.')
    except FileExistsError:
        print('O arquivo não foi encontrado')
    else:
        for i in opening_file.readlines():
            try:
                i = (int(i))
            except ValueError:
                print('Ops! Um ou mais dos valores informados não são inteiros.')
            else:
                lista_numeros.append(i)
            if len(lista_numeros) != 0:
                print(True)
                print(lista_numeros)
            else:
                print(False)
                print(None)    
def ordena_lista(nome_lista, metodo_ordena):
    pass