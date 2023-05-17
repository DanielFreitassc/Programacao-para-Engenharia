#   15- Elabore um script que crie um dicionário na qual cada chave seja um
#   caractere, e seu valor seja o número de vezes que o caractere aparece na frase.
#   Exemplo:
#   "Digite uma frase para contar as letras:“ – eu sei
#   Resposta {'e': 2, 'u': 1,
#   ' ': 1, 's': 1, 'i': 1}

palavra = input("Isira uma palavra: ")  # Aqui pedimos para o usuário definir nossa variavel.
dicionario = {}                         # Aqui criamos um dicionario vazio.
for letra in palavra:                   # Para cada letra em palavra.
    if letra in dicionario:             # Se letra estiver no dicionaro.
        dicionario[letra]+= 1           # Aqui serve para caso a letra  se repetir somar um valor a essa letra.
    else:                               # Senão.
        dicionario[letra] = 1           # Se a letra é escrita uma vez só ele entra nesse else e adiciona o valor 1 ao dicionario.
print("Reposta: ", dicionario)          # Aqui mostramos o dicionario para o usário.