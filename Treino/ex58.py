salario = float(input("Diga seu salário: "))

if salario <= 1250:
    aumento = salario * 0.15
    print(f"O Seu novo salário: {salario+aumento}")
else:
    aumento = salario * 0.10
    print(f"O seu novo salário: {salario+aumento}")
