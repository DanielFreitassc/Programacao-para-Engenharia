#   8 – Desenvolva um código em Python que adicione em um dicionário “d” os
#   seguintes campos: nome, idade, endereço e telefone e mostre os dados no
#   final.

nome = input("Nome: ")                                  # Aqui criamos uma variavel que receve o nome.
idade = input("Idade: ")                                # Aqui criamos uma variavel que receve o idade.
endereco = input("Endereço: ")                          # Aqui criamos uma variavel que receve o endereço.
telefone = input("Telefone: ")                          # Aqui criamos uma variavel que receve o telefone.

dic = {"nome": nome ,"idade" : idade,                   # Aqui criamos um dicionirio que receve os valores da variavel anterior.
        "endereço" : endereco, "telefone" : telefone}   # Aqui criamos um dicionirio que receve os valores da variavel anterior.
                                                            
print("Dados: ")                                        # Aqui mostramos para o usuário uma mensagem.
print("Nome:", dic["nome"])                             # Aqui mostramos a variavel nome dentro do dicionario.
print("Idade:", dic["idade"])                           # Aqui mostramos a variavel idade dentro do dicionario.
print("Endereço:", dic["endereço"])                     # Aqui mostramos a variavel endereço dentro do dicionario.
print("Telefone:", dic["telefone"])                     # Aqui mostramos a variavel telefone dentro do dicionario.


