Numero = int(input("Insira um número inteiro qualquer: "))
print("1 P/binário")
print("2 P/Octal")
print("3 P/Hexadecimal")
base = int(input("Insira qual base você deseja converter:"))

if base == 1:
    print(f"O número convertido é: {bin(Numero)[2:]}")
elif base == 2:
    print(f"O número convertido é: {oct(Numero)[2:]}")
else:
    print(f"O número convertido é: {hex(Numero)[2:]}")