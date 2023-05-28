nome = input("Insira seu nome: ")
recebe = float(input("Insira seu salário mensal: "))
extra = float(input("Insira um valor caso rebe algo por fora senão digite[0]"))
contas = float(input("Insira suas contas mensais: "))
continuar = input("Deseja Adicionar mais alguma coisa? [s/n]:")
conta = []
salario = []
total = recebe + extra
salario.append(total)
subtotal = salario - conta
conta.append(subtotal)
while continuar != "n":
    print("Insira Uma das opções:")
    print("1 Adicionar extra")
    print("2 Adicionar conta") 
    print("3 Sair")
    resposta = input(":")
    if resposta == "1":
        extra = float(input("Insira um valor caso rebe algo por fora senão digite[0]"))
        salario.append(extra)
    elif resposta == "2":
        contas = float(input("Insira suas contas mensais: "))
        conta.append(contas)
    else:
        break
else:
    print(f"Olá {nome} seja bem vindo(a)!")
print(f"Seu salário + o Extra é: {conta}")
if subtotal >= 0:
    print("-"*25)   
    print(f"Sobrou: {conta}")
else:
    print("-"*25)
    print(f"Você está devendo: {conta}")