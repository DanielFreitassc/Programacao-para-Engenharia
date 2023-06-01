lista = []
numero = float(input("Insira um número: "))

while numero != -1:
    if numero > 0:
     lista.append(numero)
     numero = float(input("Insira um número: "))
if len(lista) > 0:
    soma = sum(lista)
    media = soma/len(lista)
    menor = min(lista)
    maior = max(lista)
    print(f"A soma dos número é: {soma}")
    print(f"A media dos números: {media}")
    print(f"Menor número é {menor}")
    print(f"Maior número é {maior}")