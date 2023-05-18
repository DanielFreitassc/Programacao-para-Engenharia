dicionario = {}
palavra = input("Insira uma palavra: ")

for letra in palavra:
    if letra in dicionario:
        dicionario[letra] +=1
    else:
        dicionario[letra] = 1
print(f"Dicionario: {dicionario}")