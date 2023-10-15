import os, sys
here = (os.path.dirname(__file__))
here = here.replace('view','models')
sys.path.append(here)
from gerenciar_arquivos import gerenciar_arquivos
from sorting_methods import SortingMethods


class Sorting:
    __dir_atual = os.path.dirname(os.path.abspath(__file__))
    __lstValores = list() 
    
    def __init__(self):
        nome_arquivo = input("Informe o nome do arquivo .txt: ")
        if gerenciar_arquivos.verificar_existencia_arquivo(nome_arquivo):
            self.nome_arquivo = f'{self.__dir_atual}/{nome_arquivo}'
            self.__lstValores = gerenciar_arquivos.ler_arquivo_inteiros(self.nome_arquivo)
            print("O arquivo foi encontrado")
        else:
            print('O arquivo não foi encontrado')

    @property
    def lista_valores(self):
        return self.__lstValores

    def changed(self, numero):
        lista1 = self.lista_valores.copy()
        lista2 = numero       
        try:
            if lista1[1] != lista2[1]:
                if lista1[-1] != lista2[-1]:
                    print('A lista foi ordenada') 
                    return True
        except IndexError:
            lista1 = self.__lista_out
        finally:
            if lista1[1] == lista2[1]:
                if lista1[-1] == lista2[-1]:
                    print('A lista não foi ordenada') 
                    return False
    
    def ordena_lista(self, metodo_ordena='quick', nome_lista:list= None):
        if nome_lista is None:
            nome_lista = self.__lstValores.copy()

        elif nome_lista is not None:
            self.__lista_out = nome_lista.copy()
            
        if metodo_ordena == 'quick':
            self.lista_ordenada = SortingMethods.quicksort(nome_lista)
            self.changed(nome_lista)
        
        elif metodo_ordena == 'bubble':
            self.lista_ordenada = SortingMethods.bubble_sort(nome_lista)
            self.changed(nome_lista)

        elif metodo_ordena == "selection":
            self.lista_ordenada = SortingMethods.selection_sort(nome_lista)
            self.changed(nome_lista)

        elif metodo_ordena == "insertion":
            self.lista_ordenada = SortingMethods.insertion_sort(nome_lista)
            self.changed(nome_lista)

    def salvar_lista_ordenada(self, nome_arquivo):
        gerenciar_arquivos.salvar_lista_em_txt(self.lista_ordenada, nome_arquivo)
        
        if gerenciar_arquivos.verificar_existencia_arquivo(nome_arquivo):
            print('A lista foi salva com sucesso')
        
        else:
            print('Houve um erro e a lista não foi salva')


pavao = Sorting()
#pavao.ordena_lista()    # Vai usar o quick e pegar a lista que foi aberta
pavao.ordena_lista('bubble')            # Vai pegar a lista que foi aberta e usar o método escolhido
# pavao.ordena_lista('bubble', [5678945,64,894,684,894,647,984,6547,9846,7956,489,789,489,794,7,894,897,948,97,7489,7])
# Usa o método escolhido e pega a lista que foi passada
pavao.salvar_lista_ordenada('lista_ordenada')
