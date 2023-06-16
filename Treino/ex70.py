#    Crie um programa que leia o ano de nascimento de sete pessoas. 
#   No final, mostre quantas pessoas ainda não atingiram a maioridade 
#   e quantas já são maiores.

from datetime import date
atual = date.today().year
maior = 0
menor = 0
for i in range(7):  
    nasc = int(input("Em que ano a pessoa nasceu?: "))
    idade = atual - nasc
    if idade >=21:
        maior += 1
    else:
        menor += 1
print(f"{menor} Pessoas são menores de idade. {maior} Pessoas são maiores de idade.")


    
