for i in range(5):
    senha = input("Insira uma senha: ")
    tentativas = 0
    while senha != "1234":
        tentativas += i+1
        print(f"Senha incorreta você tem 5 chances, tentativa número: {i+1}")      
        if tentativas == 5:
            print(f"Conta Bloqueda!")
        break         
    else:
        print("Entrou!")
