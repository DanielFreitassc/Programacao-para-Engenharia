for i in range(1,6):
    senha = input("Digite uma senha: ")
    if senha == "1234":
        print("Bem vindo")
    else:
        print(f"Tente denovo, Total de chances {i}/5")
else:
    print("Conta bloqueada")