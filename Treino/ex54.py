distancia = float(input("Insira as distancia em kms: "))

if distancia <= 200:
     preco = distancia * 0.50
     print(f"O valor da viagem ficou: R${preco}")
else:
     preco = distancia * 0.45
     print(f"O valor da viagem ficou: R${preco}")
     