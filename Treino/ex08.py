numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in range(10):
    numeros.append(numeros)
for numero in reversed(numeros):
    print(f"Numero reverso: {numero}")