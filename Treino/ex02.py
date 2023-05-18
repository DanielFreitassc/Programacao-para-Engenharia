numero = int(input("Insira o número que quer saber a tabuada: "))

for i in range(1,11):
    resultado = numero * i 
    print(numero,"x",i, "=",resultado)
