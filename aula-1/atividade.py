import random
lista = []
for i in range(random.randint(1, 1000000)):
    lista.append(random.randint(1, 1000000))
with open('/home/pavao/Área de trabalho/progredes2023-2/aula-1/lista_nao_ordenada.txt', 'w') as arquivo:
    for i in lista:
        arquivo.writelines(str(i)+', ')
#lista com n elementos
#lista_nao_ordenada.txt