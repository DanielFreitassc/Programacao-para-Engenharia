lista = []
numero = float(input("Insira um número: "))

while numero != -1:
    if numero >0:
        lista.append(numero)
    numero = float(input("Insira um número: "))
if len(lista) > 0:
    soma = sum(lista)
    media = soma / len(lista)
    menor = min(lista)
    maior = max(lista)
    print(f"A soma é: {soma}")
    print(f"A média é: {media}")
    print(f"O menor número é: {menor}")
    print(f"O maior número é: {maior}")
else:
    print("Número invalido!")