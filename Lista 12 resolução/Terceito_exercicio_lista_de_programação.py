notas = []
alunos_media_7 = 0 

for i in range(1,11):
    print("Insira a nota do aluno: ")
    nota1 = float(input("Insira a nota: "))
    nota2 = float(input("Insira a nota: "))
    nota3 = float(input("Insira a nota: "))
    nota4 = float(input("Insira a nota: "))
    
    media = (nota1 + nota2 + nota3 + nota4)/4 
    notas.append(media)
    if media >=7:
        alunos_media_7 += 1
        print("Alunos com nota maior ou igual a 7 = {}".format(alunos_media_7))
