reta1 = float(input("Insira o primeiro lado: "))
reta2 = float(input("Insira o segundo lado: "))
reta3 = float(input("Insira o terceiro lado: "))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("sim pode formar um trinagulo!")
else:
    print("não pode formar um triangulo!")