# Módulo para funções relacionadas ao cadastro de produtos
def cadastrar_produto():
    # Implemente a lógica para cadastrar um produto
    # ...
    print("Cadastro realizado com sucesso!")

# Módulo para funções relacionadas à realização de vendas
def realizar_venda():
    # Implemente a lógica para realizar uma venda
    # ...
    print("Venda realizada com sucesso!")

# Módulo para funções relacionadas à alteração de produtos
def alterar_produto():
    # Implemente a lógica para alterar um produto
    # ...
    print("Alteração realizada com sucesso!")

# Módulo para funções relacionadas aos relatórios
def relatorio_produtos():
    # Implemente a lógica para gerar o relatório de todos os produtos
    # ...
    print("Relatório de todos os produtos")

def relatorio_vendas():
    # Implemente a lógica para gerar o relatório de vendas realizadas
    # ...
    print("Relatório de vendas realizadas")

# Função principal para exibir o menu e chamar as funções correspondentes
def menu_principal():
    while True:
        print("----- Menu Principal -----")
        print("1 - Cadastrar Produto")
        print("2 - Alterar Produto")
        print("3 - Realizar Venda")
        print("4 - Relatórios")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            alterar_produto()
        elif opcao == "3":
            realizar_venda()
        elif opcao == "4":
            print("----- Relatórios -----")
            print("1 - Relatório de todos os produtos")
            print("2 - Relatório de vendas realizadas")

            relatorio_opcao = input("Escolha uma opção de relatório: ")

            if relatorio_opcao == "1":
                relatorio_produtos()
            elif relatorio_opcao == "2":
                relatorio_vendas()
            else:
                print("Opção inválida!")
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

# Executar a função principal
menu_principal()
