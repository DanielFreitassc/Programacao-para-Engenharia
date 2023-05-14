#   3 - Desenvolva um script em linguagem Python que peça as quatro
#   notas de 10 alunos, calcule e armazene num vetor a média de cada
#   aluno, imprima o número de alunos com média maior ou igual a 7

notas = []                                                                        # Aqui criamos uma lista com nome de notas.
alunos_media_7 = 0                                                                # Aqui criamos uma variavel e atribuimos um valor a ela.   

for i in range(10):                                                               # For sera executado repetidas vezes com base no valor de range.
    print("Insira a nota do aluno: ")                                             # Aqui mostramos uma mensagem para o usuário pedindo para insirir a nota do aluno
    nota1 = float(input("Insira a nota 1: "))                                     # Aqui pedimos para o usário digitar a nota 1.
    nota2 = float(input("Insira a nota 2: "))                                     # Aqui pedimos para o usário digitar a nota 2.
    nota3 = float(input("Insira a nota 3: "))                                     # Aqui pedimos para o usário digitar a nota 3.
    nota4 = float(input("Insira a nota 4: "))                                     # Aqui pedimos para o usário digitar a nota 4.

    media = (nota1 + nota2 + nota3 + nota4)/4                                     # Aqui vamos fazer uma média com as notas.
    notas.append(media)                                                           # Aqui adicionamos a media das notas na lista notas.
    if media >=7:                                                                 # se a media for maior igual a 7 entrara no if.
        alunos_media_7 += 1                                                       # Aqui sera somado 1 a cada aluno com media maior ou igual a 7.
        print("Alunos com nota maior ou igual a 7 = {}".format(alunos_media_7))   # Aqui mostrara para o usário  a quantidades de alunos com nota maior ou igual a 7.
