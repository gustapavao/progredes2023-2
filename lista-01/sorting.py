numeros1 = [1, 8, 3, 5, 11, 21, 2, 40, 9, 4]

def bubble_sort(numeros):
    for _ in range(len(numeros)-1): #pq não há ninguém após o último
        for i in range(len(numeros)-1):
            if numeros[i] > numeros[i+1]:
                numeros[i], numeros[i+1] = numeros[i+1], numeros[i]
                print(numeros)

#bubble_sort(numeros1)

def insertion_sort(numeros):
    numeros2 = numeros
    for i in range (1, len(numeros)):
        k = numeros[i]
        j = i - 1
        while j >= 0 and numeros2[j] > k:
            numeros2[j + 1] = numeros2[j]
            j -= 1
        numeros2[j + 1] = k
        return numeros2

print(insertion_sort(numeros= numeros1))


########### EXEMPLO DO PROFESSOR ###########
#lstValores = numeros1
def insertion_sort1(numeros):
    for i in range(1, len(numeros)):
        key = numeros[i]
        j = i - 1
        while j >= 0 and numeros[j] > key:
            numeros[j + 1] = numeros[j]
            j -= 1
        numeros[j + 1] = key
########### EXEMPLO DO PROFESSOR ###########
print(insertion_sort1(numeros1))