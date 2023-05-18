numeros = []

for i in range(10):
    numero = int(input("Insira um número: "))
    numeros.append(numero)
for numero in reversed(numeros):
    print(f"O número reverso é: {numero}")