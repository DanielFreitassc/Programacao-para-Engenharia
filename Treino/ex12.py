#   Crie um programa que solicite ao usuário digitar um número e exiba todos os seus divisores.

numero = int(input("Digite um número: "))

print("Divisores de", numero, ":")

for divisor in range(1, numero + 1):
    if numero % divisor == 0:
        print(divisor)