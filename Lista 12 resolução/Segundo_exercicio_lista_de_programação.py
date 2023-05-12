lista = []                                            # Aqui criamos uma lista.
for i in range(1,11):                                 # Aqui usamos o "for" para repetir o codigo 10 vezes como solicitado na atividade.
    numero = int(input("Insira um número inteiro: ")) # Aqui recebemos o número do usuário. 
    lista.append(numero)                              # Aqui usamos a o .append() que serve para adicionar elementos a uma lista.
for numero in reversed(lista):                        # Aqui Vamos inverter os itens da lista usando o reversed():  .
    print("O Número inverso é:{}".format(numero))     # Aqui mostramos os número inversos para o usuário.
