nome = input("Insira seu nome: ").strip()
separado = nome.split()

print(f"Olá {separado[0]}")
print(f"Seu ultimo sobrenome é: {separado[len(separado)-1]}")