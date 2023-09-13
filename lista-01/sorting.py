#SOU ALUNO DE POO E PROGREDES
import os
class sorting:
    __dir_atual = os.path.dirname(os.path.abspath(__file__))
    __lstValores = None 
    
    def __init__(self, nome_arquivo):
        __file = os.path.exists((f'{self.__dir_atual}/{nome_arquivo}'))
        if __file:
            self.nome_arquivo = f'{self.__dir_atual}/{nome_arquivo}'
            # print("O arquivo foi encontrado")
            return self.__ler_arquivo(f'{self.__dir_atual}/{nome_arquivo}')
        else:
            # print('O arquivo não foi encontrado')
            return None
            
    @property
    def ListaValores(self):
        return self.__lstValores
    
    def __str__(self):
        return f"Olá usuário. Vou te ajudar a ordenar listas"
        
    
    def __ler_arquivo(self, nome_arquivo=None):
            self.__lstValores = list()
            try:
                if nome_arquivo is None:
                    nome_arquivo = self.nome_arquivo
                self.arquivo = open(self.nome_arquivo, 'r')
            except AttributeError:
                print('ERRO: A sua lista não foi gerada!')
            except:
                print('Houve um erro')
            else:
                while True:
                    v = self.arquivo.readlines()
                    if not v: break
                    for i in v:
                        try:
                            self.__lstValores.append(int(i))
                        except ValueError:
                            print('Houve um erro com um ou mais valores do arquivo')                       
                print(True)
                print(self.__lstValores)
                self.arquivo.close()
    
    def changed(self, numero):
        lista1 = self.__lstValores
        lista2 = numero
        try:
            if lista1[1] == lista2[1]:
                if lista1[-1] == lista2[-1]:
                    pass
        except IndexError:
            lista1 = self.__lista_out
        finally:
            if lista1[1] == lista2[1]:
                if lista1[-1] == lista2[-1]:
                    print('Houve um erro e a lista não ordenada!')
                    print(None)
            else:
                print(True)
                print(self.lista_ordenada)


        
    
    
    def ordena_lista(self, metodo_ordena='quick', nome_lista:list= None):
        if nome_lista is None:
            nome_lista = self.__lstValores.copy()
        elif nome_lista is not None:
            self.__lista_out = nome_lista.copy()
        if metodo_ordena == 'quick':
            self.lista_ordenada = self.quicksort(nome_lista)
            self.changed(nome_lista)
        if metodo_ordena == 'bubble':
            self.lista_ordenada = self.bubble_sort(nome_lista)
            self.changed(nome_lista)
        if metodo_ordena == "selection":
            self.lista_ordenada = self.selection_sort(nome_lista)
            self.changed(nome_lista)
        if metodo_ordena == "insertion":
            self.lista_ordenada = self.insertion_sort(nome_lista)
            self.changed(nome_lista)

    def salvar_lista_ordenada(self, nome_arquivo):
        file = open(f'{nome_arquivo}.txt', 'w')
        for i in self.lista_ordenada:
            file.writelines(f'{i}\n')
        file.close
        file_existence = f'./{nome_arquivo}.txt'
        check_file_existence = os.path.exists(file_existence)
        if check_file_existence:
            print('A lista foi salva com sucesso')
        else:
             print('Houve um erro e a lista não foi salva')    
    
    def bubble_sort(self, lista_N_ordenada):
        for _ in range(len(lista_N_ordenada)-1): #pq não há ninguém após o último
            for i in range(len(lista_N_ordenada)-1):
                if lista_N_ordenada[i] > lista_N_ordenada[i+1]:
                    lista_N_ordenada[i], lista_N_ordenada[i+1] = lista_N_ordenada[i+1], lista_N_ordenada[i]
        return lista_N_ordenada
    
    def insertion_sort(self, lista_N_ordenada):
        for i in range (1, len(lista_N_ordenada)):
            k = lista_N_ordenada[i]
            j = i - 1
            while j >= 0 and lista_N_ordenada[j] > k:
                lista_N_ordenada[j + 1] = lista_N_ordenada[j]
                j -= 1
            lista_N_ordenada[j + 1] = k
        return(lista_N_ordenada)
    
    def selection_sort(self, lista_N_ordenada):
        for i in range(len(lista_N_ordenada)):
            indice = i
            for d in range(i + 1, len(lista_N_ordenada)):
                if lista_N_ordenada[d] < lista_N_ordenada[indice]:
                    indice = d
            (lista_N_ordenada[i], lista_N_ordenada[indice]) = (lista_N_ordenada[indice], lista_N_ordenada[i])
        return(lista_N_ordenada) 
    
    def partition(self, values, low, high):
        pivot = values[high]
        i = low -1
        for j in range(low, high):
            if values[j] <= pivot:
                i += 1
                values[j], values[i] =values[i], values[j]
        (values[i+1], values[high]) = (values[high], values[i+1])
        return i+1


    def quicksort(self, values, low=0, high=None):
        if high is None:
            high = len(values)-1
        if low < high:
            p = self.partition(values, low, high)
            self.quicksort(values,low, p - 1)
            self.quicksort(values, p + 1, high)
        return values



# pavao = sorting('lista_random.txt')
# pavao.ler_arquivo()
# pavao.ordena_lista() #Vai usar o quick e pegar a lista que foi aberta
# pavao.ordena_lista('bubble')            # Vai pegar a lista que foi aberta e usar o método escolhido
# pavao.ordena_lista('bubble', [567894564,64,894,684,894,647,984,6547,9846,7956,489,789,489,794,7,894,897,948,97,7489,7]) #Usa o método escolhido e pega a lista que foi passada
# pavao.salvar_lista_ordenada('lista_ordenada.txt')

        

