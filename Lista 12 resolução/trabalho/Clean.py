atleta = input("Insira o nome do atleta: ")
notas = []
for i in range(7):
    jurados = float(input("Insira a nota do atleta: "))
    notas.append(jurados)
notas.sort()

maior = notas[-1]
menor = notas[0]
NotasTiradas = notas[1:6]
media = sum(NotasTiradas) / len(NotasTiradas)
print(f"atleta: {atleta}")
print(f"Melhor nota: {maior}")
print(f"Pior nota: {menor}")
print(f"A média das notas é: {round(media,2)}")
