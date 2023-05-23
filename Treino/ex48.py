palavra = input("Insira uma palavra: ").strip().lower()
print("A palavra A aparece:",palavra.count("a"))
print("A primeira letra parece na posição:", palavra.find("a")+1)
print("A primeira letra parece na posição:", palavra.rfind("a")+1)
