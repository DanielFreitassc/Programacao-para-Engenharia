notas = []
for i in range(1):
    nt1 = float(input(f"Digite a {i+1}° nota: "))
    nt2 = float(input(f"Digite a {i+2}° nota: "))
    notas.append(nt1)
    notas.append(nt2)
if len(notas) > 0:
    soma = sum(notas)
    media = soma / len(notas)
    maior = max(notas)
    print(f"A média das notas é : {media} a nota maior nota tirada foi: {maior}")