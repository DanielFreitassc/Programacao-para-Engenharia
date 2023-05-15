#9 – Elabore um script em linguagem Python, utilizando Dicionários, que
#contenha 4 funcionários, com o índice numérico e seu nome. Em seguida,
#solicite do usuário demitir um dos funcionários conforme o número de
#cadastro e mostre na tela os funcionários restantes.
funcionarios = {1010: "yuri", 2020 : "marcelo", 3030: "Vagner", 4040 : "michel"}                                # Aqui criamos um dicionario que relaciona o nome a um codigo.

while len(funcionarios) > 0:                                                                                    # Aquimos um laço que lê a lista de funcionario se for maior que 0, entra no while.
    print("\nFuncionários:")                                                                                    # Aqui mostramos uma mensagem para o usário.
    for codigo, nome in funcionarios.items():                                                                   # Laço codigo , nome em funcionários. 
        print(f"{codigo}: {nome}")                                                                              # Aqui mostramos o codigo e o nome do funcionário para  o usuário.

    num_cadastro = int(input("Digite o número de cadastro do funcionário a ser demitido (ou 0 para sair): "))   # Aqui pedimos para o usuário digitar o codigo do funcionário que deseja demitir.
    
    if num_cadastro == 0:                                                                                       # Se numero de cadastro for igual a 0 o codigo para.
        break                                                                                                   # Parar

    if num_cadastro in funcionarios:                                                                            # Se numero de cadastro estiver em 
        funcionarios.pop(num_cadastro)                                                                          # Aqui é removido do dicionario o número digitado pelo usuário.
        print("\n///// Funcionário demitido com sucesso! //////")                                               # Aqui mostramos uma mensagem ao usuário dizendo que o funcionário foi demitido.
    else:                                                                                                       # Aqui se  o número digitado pelo usário não  estiver no dicionario ele diz que é invalido.
        print("\nNúmero de cadastro inválido!")                                                                 # Aqui mostra ao usário uma mensagem dizendo que o númeor é invalido.

if len(funcionarios) == 0:                                                                                      # Se a lista de funcionario for igual a 0.
    print("\nTodos os funcionários foram demitidos.")                                                           # Mostra uma mensagem ao usuário dizendo que todos os funcionarios foram demitidos.

  
  