frase = "Texto teste para testes" #Variavel String frase
print(frase[:5])                  # Aqui começa mostra a frase do começo até o 4.
print(frase[5:])                  # Aqui começa do 5 até o final.
print(frase.count("o"))           # Aqui conta as letras dentro do aspas.
print(frase.upper())              # Aqui joga as frases pro maisculo.
print(frase.lower())              # Aqui joga as frases pro minusculo.
print(len(frase) )                # Aqui conta os caracteres mesmo espaços vazios.
print(frase.split())              # Aqui separa as frases.
print(frase.strip())              # Aqui tira os espaços desnecessarios da frase.
print("teste" in frase)           # Teste esta em frase: True
print(frase.find("teste"))        # Aqui mostra a localização da frase.
