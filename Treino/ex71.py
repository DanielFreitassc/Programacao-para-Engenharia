#    Faça um programa que leia o peso de cinco pessoas. 
#   No final, mostre qual foi o maior e o menor peso lidos.
from os import system
def enfeite(msg):
    print("=-"*14)
    print(f"{msg:^30}")
    print("=-"*14)
pesos = []

for i in range(1,6):
    system("cls")
    enfeite("Insira os Dados")
    peso = float(input(f"Insira o peso da {i}*, Pessoa:"))
    pesos.append(peso)
print(f"Maior peso cadastrado:{max(pesos)}")