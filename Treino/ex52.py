velocidade = float(input("Velocidade atual: "))

if velocidade > 80:
    pag = velocidade - 80
    pagar = pag * 7 
    print(f"Pagar R$ {pagar}")
