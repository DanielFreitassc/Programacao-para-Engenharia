#   10 – Elabore um script em linguagem Python que, dados dois inteiros x e y,
#   retorna uma lista com todos os valores entre x e y (inclusive), considerando x <
#   y. Exemplos x = 2, y = 6, resultado = [2, 3, 4, 5, 6]

def valores_entre(x, y):                        # Aqui nos criamos uma função com def, 
    if x >= y:                                  # se x for maior igual a y.
        return "Erro: x deve ser menor que y."  # ele retorna e diz quqe x deve ser menor que y

    lista_valores = []                          # aqui criamos uma list vazia.
    for i in range(x, y + 1):                   # laço i em raio de x y + 1
        lista_valores.append(i)                 # aqui adicionamos i a nossa lista 

    return lista_valores                        # Return é usado em uma função para especificar o valor que a função deve tomar quando é chamada.
                       
x = 2                                           # variavel x = 2
y = 6                                           # variavel y = 6
resultado = valores_entre(x, y)                 # variavel resultado é igual variavel valores entre x ,y 
print(resultado)                                # Aqui mostramos o resultado ao usúario.