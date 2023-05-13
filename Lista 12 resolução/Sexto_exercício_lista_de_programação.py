altura_pessoas = []
for i in range(15):
    altura = float(input(f"Informe a altura da pessoa {i+1}: "))
    altura_pessoas.append(altura)

menor_altura = min(altura_pessoas)
maior_altura = max(altura_pessoas)

print(f"A menor altura do grupo é: {menor_altura}")
print(f"A maior altura do grupo é: {maior_altura}")
print("Dados de entrada:")
print(altura_pessoas)