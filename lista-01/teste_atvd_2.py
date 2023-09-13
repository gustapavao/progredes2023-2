import sorting, sys

teste = sorting.sorting('lista_random2.txt')

if teste.ListaValores is None:
    print('Lista não gerada')
    sys.exit()

print(teste.ListaValores)

print(teste)
#teste.ordena_lista() #Vai usar o quick e pegar a lista que foi aberta
#teste.ordena_lista('bubble')            # Vai pegar a lista que foi aberta e usar o método escolhido
#teste.ordena_lista('bubble', [567894564,64,894,684,894,647,984,6547,9846,7956,489,789,489,794,7,894,897,948,97,7489,7]) #Usa o método escolhido e pega a lista que foi passada
#teste.salvar_lista_ordenada('lista_ordenada.txt')