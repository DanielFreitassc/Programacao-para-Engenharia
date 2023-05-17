lista = []
for i in range(10):
    numero = int(input(f"Insira um número {i+1}: "))
    lista.append(numero)
for numero in reversed(lista):
    print(numero)

