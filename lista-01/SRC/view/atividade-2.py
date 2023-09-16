#SOU ALUNO DE POO E PROGREDES
import os, sys 
here = (os.path.dirname(__file__))
here = here.replace('view','models')
sys.path.append(here)
from gerenciar_arquivos import gerenciar_arquivos
from sorting_methods import sorting_methods

class sorting:
    __dir_atual = os.path.dirname(os.path.abspath(__file__))
    __lstValores = list() 
    
    def __init__(self, nome_arquivo):
        if gerenciar_arquivos.verificar_existencia_arquivo(nome_arquivo):
            self.nome_arquivo = f'{self.__dir_atual}/{nome_arquivo}'
            self.__lstValores = gerenciar_arquivos.ler_arquivo_inteiros(self.nome_arquivo)
            print("O arquivo foi encontrado")
        else:
            print('O arquivo não foi encontrado')
            
    
    @property
    def ListaValores(self):
        return self.__lstValores
    
    
    def changed(self, numero):
        lista1 = self.ListaValores
        lista2 = numero       
        try:
            if lista1[1] != lista2[1]:
                if lista1[-1] != lista2[-1]: 
                    return True  
        except IndexError:
            lista1 = self.__lista_out
        finally:
            if lista1[1] == lista2[1]:
                if lista1[-1] == lista2[-1]:
                    return False
    
    def ordena_lista(self, metodo_ordena='quick', nome_lista:list= None):
        if nome_lista is None:
            nome_lista = self.__lstValores.copy()

        elif nome_lista is not None:
            self.__lista_out = nome_lista.copy()
            
        if metodo_ordena == 'quick':
            self.lista_ordenada = sorting_methods.quicksort(nome_lista)
            self.changed(values = nome_lista)
        
        elif metodo_ordena == 'bubble':
            self.lista_ordenada = sorting_methods.bubble_sort(nome_lista)
            self.changed(nome_lista)
        
        elif metodo_ordena == "selection":
            self.lista_ordenada = sorting_methods.selection_sort(nome_lista)
            self.changed(nome_lista)
        
        elif metodo_ordena == "insertion":
            self.lista_ordenada = sorting_methods.insertion_sort(nome_lista)
            self.changed(nome_lista)

    def salvar_lista_ordenada(self, nome_arquivo):
        gerenciar_arquivos.salvar_lista_em_txt(self.lista_ordenada, nome_arquivo)
        
        if gerenciar_arquivos.verificar_existencia_arquivo(f'{nome_arquivo}.txt'):
            print('A lista foi salva com sucesso')
        
        else:
             print('Houve um erro e a lista não foi salva')    
    
    



pavao = sorting('lista_random.txt')
#pavao.ordena_lista() #Vai usar o quick e pegar a lista que foi aberta
pavao.ordena_lista('bubble')            # Vai pegar a lista que foi aberta e usar o método escolhido
# # pavao.ordena_lista('bubble', [567894564,64,894,684,894,647,984,6547,9846,7956,489,789,489,794,7,894,897,948,97,7489,7]) #Usa o método escolhido e pega a lista que foi passada
pavao.salvar_lista_ordenada('lista_ordenada')

        

