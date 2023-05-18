#   3 - Desenvolva um script em linguagem Python que peça as quatro
#   notas de 10 alunos, calcule e armazene num vetor a média de cada
#   aluno, imprima o número de alunos com média maior ou igual a 7.

notas = []
media_final = 0
for i in range(10):
    nota_1 = float(input("Insira a primeira nota: "))
    nota_2 = float(input("Insira a segunda nota: "))
    nota_3 = float(input("Insira a terceira nota: "))
    nota_4 = float(input("Insira a quarta nota: "))
    media = (nota_1 + nota_2 + nota_3 + nota_4) / 4
    notas.append(media)
    if media >= 7:
        media_final += 1
    print(media_final)