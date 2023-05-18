#   2 - Elabore um script em linguagem Python que leia de 10 números
#   reais, inserindo-os numa lista e ao final, mostre-os na ordem inversa

lista = []

for i in range(10):
    numero = float(input("Insira um número: "))
    lista.append(numero)
for numero in reversed(lista):
    print(f"O número reverso é: {numero}")
