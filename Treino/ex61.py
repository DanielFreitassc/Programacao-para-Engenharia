login = input("Insira seu nome: ").lower()
senha = input("Insira uma senha: ")
while login != "daniel" and senha != "1234":
    login = input("Insira seu nome: ")
    senha = input("Insira uma senha: ")
else:
    print("Parabéns")    
