from random import randint
from time import sleep
itens = ("pedra","papel","tesoura")
computador = randint(0,2)
print("Suas opções:")
print("[0] PEDRA")
print("[1] PAPEL")
print("[2] TESOURA")
jogada = int(input("Qual é sua jogada? "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!")
print("-="*25)
print(f"O computador escolheu: {itens[computador]}")
print(f"O jogador escolheu: {itens[jogada]}")
print("-="*25)

if computador == 0: #Pedra
    if jogada == 0:
        print("empate!")
    elif jogada == 1:
        print("Você venceu!")
    elif jogada == 2:
        print("Computador venceu!!")
    else:
        print("Jogada invalida!")
elif computador == 1: #Papel
    if jogada == 0:
        print("Computador venceu!")
    elif jogada == 1:
        print("Empate!")
    elif jogada == 2:
        print("Você venceu!")
    else:
        print("jogada invalida!")
elif computador == 2: #Tesoura
    if jogada == 0:
        print("Você venceu!")
    elif jogada == 1:
        print("Computador venceu!")
    elif jogada == 2:
         print("Empate!")
    else:
        print("Jogada invalida")
else:
    print("erro")