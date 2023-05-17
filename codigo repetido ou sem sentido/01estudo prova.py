#    1 - Desenvolva um script Python que lê vários números
#    positivos via teclado. Quando o número lido for -1, o script
#    deve parar e exibir a soma de todos os números positivos
#    inseridos, a média desses números, o menor e o maior número
#    digitado. No entanto, utilize uma lista para armazenar os
#    números.

numeros_positivos = []
numero = float(input("Insira um  número [-1/Para parar]: "))
while numero != -1:
    if numero > 0:
        numeros_positivos.append(numero)
    numero = float(input("Insira um número [-1/Para parar]: "))
if len(numeros_positivos) > 0:
    soma = sum(numeros_positivos)
    media = soma / len(numeros_positivos)
    menor = min(numeros_positivos)
    maximo = max(numeros_positivos)
    print(f"A soma dos números é: {soma}")
    print(f"A média dos números é: {media}")
    print(f"O menor número é: {menor}")
    print(f"O maior número é: {maximo}")
else:
    print("Número invalido!")
