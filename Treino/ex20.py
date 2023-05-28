ValorCasa = float(input("Valor da casa: R$ "))
Salario = float(input("Salário: R$"))
Anos = int(input("Anos P/ pagar ?: "))

Prestação = ValorCasa/(Anos*12)
Aprovação = Salario * 0.30
if Prestação <= Aprovação: 
    print(f"Para pagar a casa de R${ValorCasa} em {Anos} anos a prestação será de R${round(Prestação,2)}!")
else:
    print("Emprestimo negado!")