peso = float(input("Insira seu peso: "))
altura = float(input("Insira sua altura: "))

imc = peso / (altura **2) 
print(imc)
if imc < 18.5:
    print("Abaixo do peso!")
elif imc >= 18.5 and imc <25:
    print("Peso ideal!")
elif imc >= 25 and imc <30:
    print(f"Seu IMC é {round(imc,2)} Sobrepeso!")
elif imc >=30 and imc < 40:
    print("Obesidade!")
else:
    print("Obesidade mórbida!")
