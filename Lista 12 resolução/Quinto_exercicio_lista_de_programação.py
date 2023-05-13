lista = [1,2,3,4,5,6,7,8,9,10]                     # Aqui criamos uma lista de 1 até o 10.
nova_lista = []                                    # Aqui criamos a nossa nova lista.
        
for numero in lista:                               # For usar os números da lista.
    if numero % 2 != 0:                            # Se o número  for dividido por ele mesmo e for diferente de 0 ele é impara e é adicionado a nova lista.
        nova_lista.append(numero)                  # Aqui adicionamos os numeros a nossa nova lista.
print(f'Lista sem números pares: {nova_lista}')    # Aqui mostramos para o usuário a lista sem os números pares.

