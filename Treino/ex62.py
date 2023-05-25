valorcasa = float(input("Insira o valor da casa: "))
salario = float(input("Insira seu salario: "))
anos = float(input("Em quantos anos pretende pagar: "))
resto = salario * 0.3
anos1 = valorcasa / anos
if resto >= anos:
    print(f"Emprestimo aprovado você pagara {resto} por {anos} anos")
else:
    print(f"Emprestimo negado!!!")


