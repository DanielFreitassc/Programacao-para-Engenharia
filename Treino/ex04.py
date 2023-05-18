#   Escreva um programa que calcule a média de uma lista de números fornecida pelo usuário.

numero = float(input("Insira o número[-1/PARA CODIGO]: "))
listamedia = []
while numero != -1:
    listamedia.append(numero)
    numero = float(input("Insira o número[-1/PARA CODIGO]: "))
    
soma = sum(listamedia)
media = soma / len(listamedia)
print(media)


   

