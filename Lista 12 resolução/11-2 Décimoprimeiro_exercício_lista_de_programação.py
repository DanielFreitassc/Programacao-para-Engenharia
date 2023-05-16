#   11 – Em um script Python com duas listas de três elementos com números
#   inteiros, crie uma nova lista onde cada elemento é a soma dos elementos de
#   mesma posição nas duas primeiras listas.
#    Exemplo: Lista1 = [1, 4, 6] Lista2 = [2, 4, 3] Lista_resultante = [3, 8, 9]

lista1 = [1,4,6]                             # Aqui criamos uma lista com trÊs elementos.
lista2 = [2,4,3]                             # Aqui criamos um lista com três elementos.
lista3 = []                                  # Aqui criamos uma lista vazia onde cada elemento é a soma dos elementos da primeira lista.

for lista1, lista2 in zip(lista1, lista2):   # Laço  lista1 lista2 combina duas ou mais sequência em pares ordenados.
    soma = lista1 + lista2                   # soma da lista 1 com a lista 2
    lista3.append(soma)                      # lista 3 adiciona o valor da soma da lista 1 com a lista 2.
print(lista3)                                # Aqui mostra ao usuário o valor da nova lista 3.