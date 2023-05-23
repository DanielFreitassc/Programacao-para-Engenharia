velocidade = int(input("velocidade: "))
if velocidade > 60 and velocidade <= 70:
    print(f"Flash!!, R$ -130,16 {velocidade}Km/h")
elif velocidade <20:
    print(f"R$ -85,13 {velocidade}Km/h")
elif velocidade >70 and velocidade <=80:
    print(f"Flash!!, R$ -195,23 {velocidade}Km/h")
elif velocidade >80 and velocidade <= 150:
    print(f"Flash!! R$ -900,34 {velocidade}Km/h")
elif velocidade >150:
    print(f"Droga é o Braian!!!!!! {velocidade}Km/h")
else:
    print(f"{velocidade}Km/h")
