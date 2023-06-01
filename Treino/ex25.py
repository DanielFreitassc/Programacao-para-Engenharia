l1 = float(input("Insira o primeiro lado do triangulo: "))
l2 = float(input("Insira a segunda nota do triangulo: "))
l3 = float(input("Insira a terceira nota do triangulo: "))

if l1 < l2 + l3 and l2 < l1 + l3  and l1 < l1 + l2:
    print("Pode formar o triângulo ", end= "")
    if l1 == l2 == l3:
        print("Equilátero!")
    elif l1 != l2 != l3 != l1:
        print("Escaleno!")
    else:
        print("Isósceles!")

else:
    print("Não pode formar um triangulo!")