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
    
print(insertion_sort([1,5,11,2,69,4,101,12,45]))