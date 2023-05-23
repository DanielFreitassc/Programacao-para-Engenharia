from random import randint
computador = randint(0,5)
numero = int(input("Chue um numero de 0 a 5: "))
while numero != computador:
   print("Erro burrao")
   numero = int(input("Chue um numero de 0 a 5: "))  
else:
    print("PARABÉNS VOCÊ ACERTOU!!!")