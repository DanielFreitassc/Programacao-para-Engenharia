numero = int(input("Digite um número no qual você deseja saber tabuada: "))
tabuada = []
print("-"*12)
for i in range(1,11):
    tb = numero * i  
    print(f"{numero} X {i} = {tb}")
print("-"*12)
    