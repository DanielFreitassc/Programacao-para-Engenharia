numero1 = float(input("Insira o 1 número: "))
numero2 = float(input("Insira o 2 número: "))
numero3 = float(input("Insira o 3 número: "))

if numero1 > numero2 and numero1 > numero3:
    print(f"O número{numero1} é o maior número digititado!")
elif numero2 > numero1 and numero2 > numero3:
    print(f"O número {numero2} é o maior número digitado!")
else: 
    print(f"O número {numero3} é o maior número digitado!")