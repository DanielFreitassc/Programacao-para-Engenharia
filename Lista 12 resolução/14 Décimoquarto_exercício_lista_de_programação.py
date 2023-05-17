#   14-Elabore um código que leia a temperatura média de cada mês do ano e
#   guarde numa lista. Com isso, efetue a média anual das temperaturas e mostre
#   todas acima da média anual, e em que mês elas ocorreram (Ex 1 – Janeiro, 2 –
#   Fevereiro, etc)

temperatura = []                                                # Aqui criamos uma lista vazia para temperatura.
mes = []                                                        # Aqui criamos uma lista vazia para o mês.

for i in range(12):                                             # Para cada i em raio de 12 que é os meses do ano.
    tempe = float(input("Insira a temperatura média do mês: ")) # Criamos uma variavel tempe que recebe a termperatura média do mês
    meses = input("Insira o nome do mês: ")                     # Aqui pedimos o nome do Mês da temperatura.
    temperatura.append(tempe)                                   # Aqui adicionamos tempe a nossa lista temperatura.
    mes.append(meses)

soma = sum(temperatura)                                         # Aqui somamos temperatura.
media = soma / len(temperatura)                                 # Aqui usamos a soma dividido pela quantidade de itens dentro da lista, usamos o len para saber quantos itens tem na lista.
print(f"A média anual de temperatura é {media}")                # Aqui mostramos na tela a temperatura média anual.
print("Meses com temperatura acima da média:")                  # Aqui mostramos uma mensagem ao usuário.                
for i in range(len(temperatura)):                               # Para cada i em raio de quantitade de itens dentro de temperatura.
    if temperatura[i] > media:                                  # Se tempera i for maior que media
        print(f"{mes[i]}: {temperatura[i]}")                    # Mostra na tela mes e temperatura do mês que é maior que a média.