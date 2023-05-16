#   6 - Dadas duas listas P1 e P2, ambas com n valores reais que representam as
#   notas de uma turma na prova 1 e na prova 2, respectivamente. Escreva um
#   script em linguagem Python que calcule a média da turma nas provas 1 e 2,
#   imprimindo em qual das provas a turma obteve a melhor média. Exemplo:
#   Tamanho da turma: 5
#   P1: 7.0 8.3 10.0 6.5 9.3 P2: 8.5 6.9 5.0 7.5 9.8
#   Resposta:
#   Média da turma na prova 1: 8.22
#   Média da turma na prova 2: 7.54
#   A turma obteve a melhor média na prova 1

lista_p1 = []                                                              # Aqui criamos uma lista para a prova 1
lista_p2 = []                                                              # Aqui criamos uma lista para a prova 2
    
print("Insira a nota da primeira prova")                                   # Aqui mostramos uma mensagem indicando oque o usuário deve fazer.
for i in range(5):                                                         # Aqui dizemos quantas vezes a mensagem vai rodar com base no range.
    nota = float(input(f"Insira a nota {i+1}: "))                          # Aqui criamos uma variavel nota que recebe as notas da primeira prova.
    lista_p1.append(nota)                                                  # Aqui adicionamos a nota a lista 1.
    soma = sum(lista_p1)                                                   # Aqui somamos os valores da lista 1.
    media_1 = soma / len(lista_p1)                                         # Aqui tiramos a média que é a soma da lista 1 dividido pela quantidade de itens da lista.
print("Insira a nota da segunda prova")                                    # Aqui mostramos uma mensagem indicando oque o usuário deve fazer.
for i in range(5):                                                         # Aqui dizemos quantas vezes a mensagem vai rodar com base no range.
    nota = float(input(f"Insira a nota {i+1}: "))                          # Aqui criamos uma variavel que recebe as notas da segunda prova.
    lista_p2.append(nota)                                                  # Aqui Adicionamos as notas da segunda prova a lista de provas 2.
    soma = sum(lista_p2)                                                   # Aqui somamos o valor da segunda lista de prova.
    media_2 = soma / len(lista_p2)                                         # Aqui tiramos a média da segunda prova.
                                           
print(f"Média da turma na prova 1:{media_1}")                              # Aqui mostramos ao usuario a média da primera prova.
print(f"Média da turma na prova 2:{round(media_2,2)}")                     # Aqui mostramos ao usuário a média da segunda prova.
if media_1 > media_2:                                                      # Se a media da primeira prova for maior que a média da segunda ela entra no if e mosta a mensagem.
    print(f"A turma obteve a melhor média na prova 1! Média: {media_1}")   # Aqui mostramos a média da primeira prova caso ela seja maior que a segunda.
else:                                                                      # Senão.
    print(f"A turma obteve a melhor média na prova 2! Média: {media_2}")   # Mostramos a média da segunda prova.