#    1 - Desenvolva um script Python que lê vários números
#    positivos via teclado. Quando o número lido for -1, o script
#    deve parar e exibir a soma de todos os números positivos
#    inseridos, a média desses números, o menor e o maior número
#    digitado. No entanto, utilize uma lista para armazenar os
#    números.

numeros = []                                                           # Aqui criamos uma lista.
numero = int(input("Insira um número! [-1/Para o codigo]: "))      # Aqui pedimos para o usuário um número inteiro positvo. 
                                                                    
while numero != -1:                                                    # Aqui dizemos em codigo: Enquanto numero não for -1 o codigo ira repetir.
    if numero >0:                                                      # Se numero for maior que 0.
        numeros.append(numero)                                         # Ele adicionara o numero a lista.
    numero = int(input("Insira um número! [-1/Para o codigo]: "))      # Aqui pedimos para o usuário um número inteiro positvo. 
if len(numeros) > 0:                                                   # se tamanho da lista for maior que 0 o codigo abaixo sera executado.
    soma = sum(numeros)                                                # Aqui somamos os elementos da lista usando o sum().
    media = soma/len(numeros)                                          # Aqui dividimos soma por len() que é a soma pela lista.
    minimo = min(numeros)                                              # Aqui usamos min() para selecionar o menor número da lista.
    maximo = max(numeros)                                              # Aqui usamos max() para selecionar o maior número da lista.
    print(f"A soma é = {soma}")                                        # Aqui mostramos o resultado na tela de soma.
    print(f"A media é = {media}")                                      # Aqui mostramos o resultado na tela de media.
    print(f"O menor número é = {minimo}")                              # Aqui mostramos o resultado na tela do menor número.
    print(f"O maior número é = {maximo}")                              # Aqui mostramos o resultado na tela do maior número.
else:                                                                  # Senão, se numero não for diferente de -1 o "else:" entra em ação.
    print("Não é um número inteiro positivo")                          # Aqui mostra na tela uma mensagem para o usuário.