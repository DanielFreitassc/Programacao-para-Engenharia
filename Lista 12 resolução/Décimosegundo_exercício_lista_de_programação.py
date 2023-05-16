#   12 – Desenvolva um script em linguagem Python, utilizando Dicionários, que
#   solicite ao usuário inserir o nome de três produtos de mercado e seus
#   respectivos preços e os mostre na tela.    

produtos = {                                                        # Aqui criamos um dicionario
    "Maçã": 2.50,                                                   # Produto e valor.                               
    "Pão": 3.20,                                                    # Produto e valor.
    "Leite": 5.75,                                                  # Produto e valor.
    "Chocolate" : 7,                                                # Produto e valor.
    "Bombom" : 10,                                                  # Produto e valor.
    "Carne" : 30                                                    # Produto e valor.
}

itens_comprador = {}                                                # Aqui crimos um dicionario vazio.

for i in range(3):                                                  # Para cara i em raio de 3.
    nome_produto = input("Insira o nome do produto: ")              # Aqui criamos uma variavel com nome de nome_produto que recebe uma string do usuário.
    itens_comprador[nome_produto] = produtos.get(nome_produto)      # Aqui chamamos o dicionario e ele retorna o valor de uma chave.

print("Produtos e Preços:")                                         # Aqui mostramos uma mensagem ao usuário.
for produto, preco in itens_comprador.items():                      # Para cada produto e preço em dicionario.
    print(f"{produto}: R${preco}")                                  # Aqui mostramos o produto e o preço ao usuário.
