notas = []
media1 = 0

for i in range(5):
    print(f"Aluno {i+1}")
    nota1 = float(input("Insira a nota 1: "))
    nota2 = float(input("Insira a nota 2: "))
    nota3 = float(input("Insira a nota 3: "))
    nota4 = 7
    
    media = (nota1 + nota2 + nota3 + nota4) / 4
    notas.append(media)
    if media >= 7:
        media1 += 1
        print(media1)