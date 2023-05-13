lista = []                                              # Aqui Criamos uam lista para a altura

for i in range(5):                                     # Aqui dizemos que for repetira 15 vezes pedindo a altura.
    altura = float(input(f"Insira sua altura {i+1}: ")) # Aqui criamos uma variavel altura que pede a altura ela repetira tantas vezes o valor de range
    lista.append(altura)                                # Aqui adicionamos a varivel altura na lista.
                                                        
menor = min(lista)                                  # Aqui tiramos a menor altura da lista.
maior = max(lista)                                  # Aqui tiramos a maior altura da lista.
       
print(f"Menor altura: {menor}")                         # Aqui mostramos ao usuário a menor altura.
print(f"Maior altura: {maior}")                         # Aqui mostramos ao usuário a maior altura.
print(f"Dados cadastrados: {lista}")                    # Aqui mostramos os dados cadastrados pelos usuários.