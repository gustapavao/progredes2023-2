import gerenciar_arquivos

class quicksort_auxiliar:
    def partition(values, low, high):
        pivot = values[high]
        i = low -1
        for j in range(low, high):
            if values[j] <= pivot:
                i += 1
                values[j], values[i] =values[i], values[j]
        (values[i+1], values[high]) = (values[high], values[i+1])
        return i+1


    def quicksort(values, low=0, high=None):
        if high is None:
            high = len(values)-1
        if low < high:
            p = sorting_methods.partition(values, low, high)
            sorting_methods.quicksort(values,low, p - 1)
            sorting_methods.quicksort(values, p + 1, high)
        return values

class sorting_methods:
    def bubble_sort(lista_N_ordenada):
        for _ in range(len(lista_N_ordenada)-1):
            for i in range(len(lista_N_ordenada)-1):
                if lista_N_ordenada[i] > lista_N_ordenada[i+1]:
                    lista_N_ordenada[i], lista_N_ordenada[i+1] = lista_N_ordenada[i+1], lista_N_ordenada[i]
        return lista_N_ordenada
    
    def insertion_sort(lista_N_ordenada):
        for i in range (1, len(lista_N_ordenada)):
            k = lista_N_ordenada[i]
            j = i - 1
            while j >= 0 and lista_N_ordenada[j] > k:
                lista_N_ordenada[j + 1] = lista_N_ordenada[j]
                j -= 1
            lista_N_ordenada[j + 1] = k
        return(lista_N_ordenada)
    
    def selection_sort(lista_N_ordenada):
        for i in range(len(lista_N_ordenada)):
            indice = i
            for d in range(i + 1, len(lista_N_ordenada)):
                if lista_N_ordenada[d] < lista_N_ordenada[indice]:
                    indice = d
            (lista_N_ordenada[i], lista_N_ordenada[indice]) = (lista_N_ordenada[indice], lista_N_ordenada[i])
        return(lista_N_ordenada) 
    
    def partition(values, low, high):
        pivot = values[high]
        i = low -1
        for j in range(low, high):
            if values[j] <= pivot:
                i += 1
                values[j], values[i] =values[i], values[j]
        (values[i+1], values[high]) = (values[high], values[i+1])
        return i+1


    def quicksort(values, low=0, high=None):
        if high is None:
            high = len(values)-1
        if low < high:
            p = quicksort_auxiliar.partition(values, low, high)
            quicksort_auxiliar.quicksort(values,low, p - 1)
            quicksort_auxiliar.quicksort(values, p + 1, high)
        return values