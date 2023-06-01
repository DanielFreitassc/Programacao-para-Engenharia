print("=====STARBUCKS=====")
produto = float(input("Insira o valor do produto: "))
print(" [1] à vista dinheiro/cheque \n [2] á vista  cartão \n [3] 2x no cartão \n [4] 3x no cartão \n Qual das opções?")
try:
    pag = int(input("Insira a forma de pagamento: "))
    if pag == 1:
        desconto = produto - (produto * 10/100)
        print(f"O valor final do produto: {desconto}")
    elif pag == 2:
        desconto = produto - (produto * 5/100)
        print(f"O valor final do produto: {desconto}") 
    elif pag == 3:
        print(f"O valor final do produto: {produto}")
    elif pag == 4:
        desconto = produto + (produto * 20/100)
        print(f"O valor final {desconto}")
    else:
        print("404 Not Found")
except ValueError:
    print('Valor não existente')


