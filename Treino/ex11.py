n_dgt = []
numero = float(input("Digite um número: "))

while numero != 3:
    n_dgt.append(numero)
    numero = float(input("Digite um número: "))
    soma = sum(n_dgt)
else:
    print("Você acertou!","Números chutados até acertar: ",n_dgt,"E a soma dos valores chutados é:",soma)
