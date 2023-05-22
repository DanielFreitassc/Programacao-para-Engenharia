import random
lista = ["daniel" , "carlos" , "luiz"]
lista1 = []
alt = random.choice(lista)
alt1 = random.choice(lista)
alt2 = random.choice(lista)
alt3 = random.choice(lista)
lista1.append(alt)
lista1.append(alt1)
lista1.append(alt2)
lista1.append(alt3)
print(f"O sorteado é: {lista1}")