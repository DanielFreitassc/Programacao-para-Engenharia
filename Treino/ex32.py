import requests
import json

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()
cotacao_dolar = cotacoes['USDBRL']["bid"]

real = int(input("Quanto dinheiro você tem na carteira? R$ "))
conversao = real / len(cotacoes)
print(f"Com {real} você pode comprar US${conversao: .2f}")