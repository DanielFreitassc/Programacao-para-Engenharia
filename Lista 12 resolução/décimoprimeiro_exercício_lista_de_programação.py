#   11 – Em um script Python com duas listas de três elementos com números
#   inteiros, crie uma nova lista onde cada elemento é a soma dos elementos de
#   mesma posição nas duas primeiras listas.
#    Exemplo: Lista1 = [1, 4, 6] Lista2 = [2, 4, 3] Lista_resultante = [3, 8, 9]

lista1 = [1,4,6]                             #
lista2 = [2,4,3]                             #
lista3 = []                                  #

for lista1, lista2 in zip(lista1, lista2):   #
    soma = lista1 + lista2                   #
    lista3.append(soma)                      #
print(lista3)                                #