numeros1 = [1, 8, 3, 5, 11, 21, 2, 40, 9, 4]

# def bubble_sort(numeros):
#     for _ in range(len(numeros)-1): #pq não há ninguém após o último
#         for i in range(len(numeros)-1):
#             if numeros[i] > numeros[i+1]:
#                 numeros[i], numeros[i+1] = numeros[i+1], numeros[i]
#                 print(numeros)

# #bubble_sort(numeros1)

# def insertion_sort(values):
#     for i in range (1, len(values)):
#         k = values[i]
#         j = i - 1
#         while j >= 0 and values[j] > k:
#             values[j + 1] = values[j]
#             j -= 1
#         values[j + 1] = k
#     print(values)
        
# insertion_sort(values= numeros1)


# ########### EXEMPLO DO PROFESSOR ###########
# #lstValores = numeros1
# def insertion_sort1(numeros):
#     for i in range(1, len(numeros)):
#         key = numeros[i]
#         j = i - 1
#         while j >= 0 and numeros[j] > key:
#             numeros[j + 1] = numeros[j]
#             j -= 1
#         numeros[j + 1] = key
# ########### EXEMPLO DO PROFESSOR ###########
# print(insertion_sort1(numeros1))

#def selection_sort(values):
#     for i in range(len(values)):
#         indice = i
#         for d in range(i + 1, len(values)):
#             if values[d] < values[indice]:
#                 indice = d
#         (values[i], values[indice]) = (values[indice], values[i])
#     print(values)   

# selection_sort(numeros1)

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
        p = partition(values, low, high)
        quicksort(values,low, p - 1)
        quicksort(values, p + 1, high)
    # except:
    #     print(False)
    #     print(None)
    # else:
    #     print(True)
    #     print(values)


quicksort(numeros1)