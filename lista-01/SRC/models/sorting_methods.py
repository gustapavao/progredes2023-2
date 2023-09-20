import gerenciar_arquivos


class QuicksortAuxiliar:
    def partition(values, low, high):
        pivot = values[high]
        i = low - 1
        for j in range(low, high):
            if values[j] <= pivot:
                i += 1
                values[j], values[i] = values[i], values[j]
        (values[i+1], values[high]) = (values[high], values[i+1])
        return i+1

    def quicksort(values, low=0, high=None):
        if high is None:
            high = len(values)-1
        if low < high:
            p = SortingMethods.partition(values, low, high)
            SortingMethods.quicksort(values,low, p - 1)
            SortingMethods.quicksort(values, p + 1, high)
        return values


class SortingMethods:
    def bubble_sort(lista_n_ordenada):
        for _ in range(len(lista_n_ordenada)-1):
            for i in range(len(lista_n_ordenada)-1):
                if lista_n_ordenada[i] > lista_n_ordenada[i+1]:
                    lista_n_ordenada[i], lista_n_ordenada[i+1] = lista_n_ordenada[i+1], lista_n_ordenada[i]
        return lista_n_ordenada
    
    def insertion_sort(lista_n_ordenada):
        for i in range(1, len(lista_n_ordenada)):
            k = lista_n_ordenada[i]
            j = i - 1
            while j >= 0 and lista_n_ordenada[j] > k:
                lista_n_ordenada[j + 1] = lista_n_ordenada[j]
                j -= 1
            lista_n_ordenada[j + 1] = k
        return(lista_n_ordenada)
    
    def selection_sort(lista_n_ordenada):
        for i in range(len(lista_n_ordenada)):
            indice = i
            for d in range(i + 1, len(lista_n_ordenada)):
                if lista_n_ordenada[d] < lista_n_ordenada[indice]:
                    indice = d
            (lista_n_ordenada[i], lista_n_ordenada[indice]) = (lista_n_ordenada[indice], lista_n_ordenada[i])
        return(lista_n_ordenada)
    
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
            p = QuicksortAuxiliar.partition(values, low, high)
            QuicksortAuxiliar.quicksort(values,low, p - 1)
            QuicksortAuxiliar.quicksort(values, p + 1, high)
        return values