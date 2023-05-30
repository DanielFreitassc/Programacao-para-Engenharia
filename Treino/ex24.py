from datetime import date 
atual = date.today().year
nascimento = int(input("Ano de nascimento: "))
idade = atual - nascimento  
print(f"O atetla tem: {idade}")
if idade <9:
    print("Mirim")
elif idade >9 and idade <=14:
    print("Infantil")
elif idade >14 and idade <=19:
    print("Junior")
elif idade >19 and idade <=25:
    print("Sênior")
else:
    print("Master")