#  7 - Construa um script em linguagem Python que utilize um dicionário
#  cujas chaves são os códigos do produto e os valores são o nome do
#  produto, o preço unitário e a quantidade comprada. A partir do
#  dicionário, o programa deve imprimir os itens da compra e calcular o
#  subtotal de cada um deles, ou seja, quantidade * preço unitário. Por fim,
#  o programa deve apresentar o valor total da compra

# Dicionário com os itens da compra e seus preços unitários
produtos = {}                                           # Aqui criamos um dicionario vazio para produtos.

while True:                                             # Aqui criamos um laço de repetição: 
    cod = int(input("Codigo: "))                        # Aqui criamos uma variavel e pedimos para o usuário definir a mesma.
    nome = input("Nome: ")                              # Aqui criamos uma variavel e pedimos para o usuário definir a mesma.
    preco = float(input("R$: "))                        # Aqui criamos uma variavel e pedimos para o usuário definir a mesma.
    qtde = int(input("Qtde: "))                         # Aqui criamos uma variavel e pedimos para o usuário definir a mesma.
    prod = []                                           # Aqui criamos uma lista vazia.
    prod.append(nome)                                   # Aqui adicionamos nome dentro da lista prod.
    prod.append(preco)                                  # Aqui adicionamos preço dentro da lista prod.
    prod.append(qtde)                                   # Aqui adiconamos quantidade dentro da lista prod.
    produtos.update({cod: prod})                        # Aqui fazemos um updateno dicionario adicionado o codigo e lista prod.
    resp = input("Deseja continuar [S/N]? ")            # Aqui fazemos uma pergunta ao usário se ele quer continaur, caso a resposta for n o codigo para.
    if resp.lower() == "n":                             # Se resposta acima for N o codigo para, obs: .lower joga as letras para minusculo, se o usuário digitar um "N" ou um "n" o script vai entender que n minusculo.
        break                                           # Aqui usamos break para parar. 
total = 0                                               # Aqui criamos uma variavel total = 0.
for cod, prod in produtos.items():                      # Para cada codigo , produto dentro da lista de produto.
    subtotal = produtos[cod][1] * produtos[cod][2]      # Aqui criamos uma variavel para calcular o subtotal.
    print(f"{prod[0]}: R$ {subtotal: .2f}")             # Aqui mostramos na tela o produto e o subtotal.
    total += subtotal                                   # Aqui somamos o subtotal ao total a cada vez que o codigo executa.
print(20 * "-")                                         # Aqui fizemos um detalhe estetico onde o "-" sera repetido 20 vezes..
print(f"Total: R$ {total: .2f}")                        # Aqui mostramos o total, o .2f  é uma formatação usada para exibir um número em formato de ponto flutuante com duas casas decimais após o ponto.