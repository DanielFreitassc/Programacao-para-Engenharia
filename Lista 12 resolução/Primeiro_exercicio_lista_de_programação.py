numeros = []                                                        # Aqui criamos uma lista.
numero = int(input("Insira um número inteiro positivo: "))          # Aqui pedimos para o usuário um número inteiro positvo. 
                                                                    
while numero != -1:                                                 # Aqui dizemos em codigo: Enquanto numero não for -1 o codigo ira repetir.
    if numero >0:                                                   # Se numero for maior que 0.
        numeros.append(numero)                                      # Ele adicionara o numero a lista.
    numero = int(input("Insira um número inteiro positivo: "))      # Aqui pedimos para o usuário um número inteiro positvo. 
if len(numeros) > 0:                                                # se tamanho da lista for maior que 0 o codigo abaixo sera executado.
    soma = sum(numeros)                                             # Aqui somamos os elementos da lista usando o sum().
    media = soma/len(numeros)                                       # Aqui dividimos soma por len() que é a soma pela lista.
    minimo = min(numeros)                                           # Aqui usamos min() para selecionar o menor número da lista.
    maximo = max(numeros)                                           # Aqui usamos max() para selecionar o maior número da lista.
    print("A soma é = {}".format(soma))                             # Aqui mostramos o resultado na tela de soma.
    print("A media é = {}".format(media))                           # Aqui mostramos o resultado na tela de media.
    print("O menor número é = {}".format(minimo))                   # Aqui mostramos o resultado na tela do menor número.
    print("O maior número é = {}".format(maximo))                   # Aqui mostramos o resultado na tela do maior número.
else:                                                               # Senão, se numero não for diferente de -1 o "else:" entra em ação.
    print("Não é um número inteiro positivo")                       # Aqui mostra na tela uma mensagem para o usuário.