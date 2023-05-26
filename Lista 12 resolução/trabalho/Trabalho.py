atleta = input("Insira o nome do atleta: ")
notas = []
for i in range(7):
    jurados = float(input("Insira a nota do atleta: "))
    notas.append(jurados)
notas.sort()
if len(notas) > 0:
    MaiorNota = max(notas)
    MenorNota = min(notas)
    maior = [-1]
    menor = [0]
    NotasTiradas = notas[1:6]
    media = sum(NotasTiradas) / len(NotasTiradas)
    print(f"atleta: {atleta}")
    print(f"Melhor nota: {MaiorNota}")
    print(f"Pior nota: {MenorNota}")
    print(f"A média das notas é: {round(media,2)}")


    