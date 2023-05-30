nota1 = float(input("Insira a primeira nota do aluno: "))
nota2 = float(input("Insira a segunda nota do aluno: "))
media = (nota1 + nota2) / 2
if media >= 7:
    print("Parabéns você passou!")
elif media <5:
    print("Reprovado!")
else:
    print("Você ficou em recuperação!")