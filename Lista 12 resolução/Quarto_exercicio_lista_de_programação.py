#   4 - Crie um script em linguagem Python que leia dois vetores com 5
#   elementos cada. Gere um terceiro vetor de 10 elementos, cujos
#   valores deverão ser compostos pelos elementos intercalados dos dois
#   outros vetores. Exibir na tela todos os vetores em linhas separadas.

vetor_1 = []                                    # Aqui criamos uma lista vazia que sera o primeiro vetor.
vetor_2 = []                                    # Aqui Criamos uma lista vazia que sera o segundo vetor.
                                            
print("Digite os elementos do primeiro vetor")  # Aqui mostramos ao usuário uma mensagem pendindo um elemento.
for i in range(5):                              # For sera executado repetidas vezes com base no valor de range.
    elemento = int(input(f"Elemento{i+1}: "))   # Aqui pedimos para o usário digitar um valor para o elemento e usamos i+1 para cada vez que o codigo repetir aparecer um feedback para o usuário saber quantas vezes ja foi repetido.
    vetor_1.append(elemento)                    # Aqui adicionamos o valor do elemento digitado pelo usuario a nossa lista (vetor_1).
print("Digite os elementos do segundo vetor")   # Aqui mostramos na tela uma mensagem pedindo para digitar os valores do segundo vetor.
for i in range(5):                              # For sera executado repetidas vezes com base no valor de range.
    elemento = int(input(f"Elemento {i+1}:"))   # Aqui pedimos para o usuário digitar um novo elemento e usamos i+1 para cada vez que o codigo repetir aparecer um feedback para o usuário saber quantas vezes ja foi repetido.
    vetor_2.append(elemento)                    # Aqui adicionamos o novo elemento ao segundo vetor.
vetor_3 = []                                    # Aqui criamos o vetor de numero 3.
for i in range(5):                              # For sera executado repetidas vezes com base no valor de range.
    vetor_3.append(vetor_1[i])                  # Aqui adicionamos o vetor 1 ao vetor 3
    vetor_3.append(vetor_2[i])                  # Aqui adicionamos o vetor 2 ao vetor 3 
print(f"Primeiro Vetor: {vetor_1}")             # Aqui mostramos uma mensagem para o usuário mostrando o primeiro vetor.
print(f"Segundo Vetor: {vetor_2}")              # Aqui mostramos uma mensagem para o usuário mostrando o segundo vetor.
print(f"Terceiro Vetor: {vetor_3}")             # Aqui mostramos uma mensagem para o usuário mostrando o terceiro vetor. 

