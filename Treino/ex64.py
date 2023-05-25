idade = int(input("Data de nascimento: "))
if idade >= 2013:
    print("Mirim")
elif idade <2013 and idade >= 2008:
    print("Infantil")
elif idade <2008 and idade >=2003:
    print("junior")
elif idade <2003 and idade >=2002:
    print("Sênior")
else:
    print("Master")