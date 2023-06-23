from sys import exit    # Importa a função `exit` da biblioteca `sys`.
import json             # Importa a biblioteca `json`, usada para Notação de Objetos JavaScript.
from os import system   # Importa a função `system` da biblioteca `os`.

banco_de_dados = 'bancodedados.json'    # Variável que armazena o nome do arquivo do banco de dados.
estoque = {}                            # Dicionário para armazenar o inventário. 
vendas = []                             # Lista para armazenar as vendas.

try:                                                                        # Trata o erro de arquivo não encontrado.                                                               
    with open(banco_de_dados, 'r', encoding='utf8') as estoquedosistema:    
        dados = json.load(estoquedosistema)                                 # Carrega os dados do arquivo JSON.
        estoque = dados.get("estoque", {})                                  # Obtém o dicionário de estoque do arquivo, ou um dicionário vazio se não houver.
        vendas = dados.get("vendas", [])                                    # Obtém a lista de vendas do arquivo, ou uma lista vazia se não houver.
except FileNotFoundError:                                                   
    with open(banco_de_dados, 'w') as estoquedosistema:                     
        json.dump({"estoque": estoque, "vendas": vendas}, estoquedosistema) # Cria um novo arquivo JSON com estoque e vendas vazios.

# Função para exibir uma mensagem de título formatada.
def titulo(msg):                                                                                  
    print("=-" * 15)    
    print(f"{msg:^30}") 
    print("=-" * 15)            
# Função para exibir uma mensagem de erro.
def erro(con):          
    print(f"{con} Erro: opção não encontrada")  

# Função para verificar se uma string pode ser convertida para um determinado tipo numérico.
def func_verifica_numero(num, tipo):            
    tester, verify = isnumber(num, tipo)        # Verifica se a string é um número válido do tipo especificado.
    if verify:                                  # Se a conversão falhou, solicita uma entrada válida do usuário.
        while tester:                           
            num = input("ERROR! Digite um número válido: ").replace(",", ".")   
            tester, verify = isnumber(num, tipo)                                # Verifica novamente a validade da nova entrada.                                                    
        return tipo(num)    # Converte o número válido para o tipo especificado.                                                       
    else:                                                                                     
        return tipo(num)    # Se a conversão foi bem-sucedida, retorna o número convertido.                                                     

# Função auxiliar para verificar se uma string é um valor numérico válido de um determinado tipo.
def isnumber(num, tipo):          
    try:                    
        tipo(num)           # Tenta converter a string para o tipo numérico especificado.
        return False, False # Se a conversão for bem-sucedida, retorna "False" para indicar que não houve erro.
    except ValueError:      
        return True, True   # Se a conversão falhou, retorna "True" para indicar um erro.

# Função para cadastrar um novo produto.
def cadastrar_produto():    #
    system("cls")           # Limpa a tela do console.
    titulo("CADASTRAR PRODUTO")                     # Exibe o título da seção.
    nome = input("Nome do produto: ").capitalize()  # Solicita o nome do produto ao usuário.
    tipo = input("Tipo do produto: ")               # Solicita o tipo do produto ao usuário.
    valor = func_verifica_numero(input("Preço de venda: ").replace(",", "."), float)    # Solicita o preço de venda ao usuário.
    estoque_inicial = func_verifica_numero(input("Quantos itens em estoque?: "), int)   # Solicita a quantidade em estoque ao usuário.

    if nome and tipo and valor and estoque_inicial: # Verifica se todos os campos obrigatórios foram preenchidos.
        identificador = len(estoque) + 1            # Gera um identificador único para o novo produto.
        estoque[identificador] = {                  # Adiciona o produto ao dicionário de estoque.
            "nome": nome,                           
            "tipo": tipo,                              
            "valor": valor,                         
            "quantidade": estoque_inicial           
        }                                           
        print("Cadastro realizado com sucesso!")    # Exibe uma mensagem de sucesso.
    else:                                           
        print("Campos obrigatórios não preenchidos.")           # Exibe uma mensagem de erro se algum campo obrigatório estiver vazio.

# Função para realizar uma venda.
def realizar_venda():                                           
    system("cls")                                               # Limpa a tela do console.
    titulo("REALIZAR VENDA")                                    # Exibe o título da seção.
    nome = input("Digite o nome do produto a ser vendido: ")    # Solicita o nome do produto a ser vendido.

    for identificador, produto in estoque.items():              # Percorre o dicionário de estoque.
        if produto['nome'].lower() == nome.lower():             # Verifica se o nome do produto corresponde ao digitado pelo usuário.
            quantidade = func_verifica_numero(input(f"Quantidade desejada ({produto['quantidade']} em estoque): "), int)    # Solicita a quantidade desejada ao usuário.

            if quantidade <= produto['quantidade']:             # Verifica se a quantidade desejada está disponível no estoque.                                                                        
                produto['quantidade'] -= quantidade             # Subtrai a quantidade vendida do estoque.
                valor_total = produto['valor'] * quantidade     # Calcula o valor total da venda.
                venda = {                                       # Cria um dicionário para armazenar os detalhes da venda.
                    "identificador_produto": identificador,     
                    "nome_produto": produto['nome'],            
                    "quantidade_vendida": quantidade,           
                    "valor_total": valor_total                  
                }
                vendas.append(venda)                            #  Adiciona a venda à lista de vendas.                   
                print(f"Venda de {nome} realizada com sucesso! Valor total: R${valor_total:.2f}")   # Exibe uma mensagem de sucesso.
            else:                                                                                   # Exibe uma mensagem de erro se a quantidade desejada não estiver disponível.
                print("Quantidade insuficiente em estoque.")                                        # Retorna após concluir a venda.
            return                                                                                  # Exibe uma mensagem de erro se o produto não for encontrado.
    else:                                                                                           
        print("Produto não encontrado.")               

# Função para alterar os detalhes de um produto.
def alterar_produto():                                                                              
    system("cls")                                                                                   # Limpa a tela do console.
    titulo("ALTERAR PRODUTO")                                                                       # Exibe o título da seção.
    nome = input("Digite o nome do produto a ser alterado: ")                                       # Solicita o nome do produto a ser alterado.

    for identificador, produto in estoque.items():                                                  # Percorre o dicionário de estoque.                                         
        if produto['nome'].lower() == nome.lower():                                                 # Verifica se o nome do produto corresponde ao digitado pelo usuário.
            novo_nome = input(f"Novo nome ({produto['nome']}): ").capitalize()                      # Solicita o novo nome do produto ao usuário.                          
            novo_tipo = input(f"Novo tipo ({produto['tipo']}): ")                                   # Solicita o novo tipo do produto ao usuário.
            novo_valor = func_verifica_numero(input(f"Novo preço de venda ({produto['valor']}): ").replace(",", "."), float)    # Solicita o novo valor do produto ao usuário.
            novo_estoque = func_verifica_numero(input(f"Novo estoque ({produto['quantidade']}): "), int)                        # Solicita a nova quantidade em estoque ao usuário.

            if novo_nome:                               # Verifica se há um novo nome fornecido                                                                                             
                produto['nome'] = novo_nome             # Atualiza o nome do produto com o novo nome
            if novo_tipo:                               # Verifica se há um novo tipo fornecido   
                produto['tipo'] = novo_tipo             # Atualiza o tipo do produto com o novo tipo         
            if novo_valor:                              # Verifica se há um novo valor fornecido
                produto['valor'] = novo_valor           # Atualiza o valor do produto com o novo valor
            if novo_estoque:                            # Verifica se há um novo estoque fornecido
                produto['quantidade'] = novo_estoque    # Atualiza a quantidade em estoque do produto com o novo estoque

            print("Alteração realizada com sucesso!")   # Exibe uma mensagem de sucesso para indicar que a alteração foi realizada
            return                                      # Retorna ao chamador da função
    else:                                               # Caso o produto não seja encontrado no estoque
        print("Produto não encontrado.")                # Exibe uma mensagem informando que o produto não foi encontrado

def relatorio_produtos():                               
    system("cls")                                       # Limpa a tela do console
    titulo("RELATÓRIO DE PRODUTOS")                     # Exibe o título do relatório de produtos
    print("1 - Relatório de todos os produtos.")        # Exibe a opção de relatório de todos os produtos
    print("2 - Relatório de vendas realizadas.")        # Exibe a opção de relatório de vendas realizadas

    opcao = input("Digite o número da opção desejada: ")    # Recebe a opção selecionada pelo usuário          
    opcao = func_verifica_numero(opcao, int)                # Verifica se a opção é um número válido

    match opcao:                                            # Verifica a opção selecionada
        case 1:                                             # Caso a opção seja 1 (relatório de todos os produtos)
            print("{:<10} {:<20} {:<15} {:<10} {:<10}".format("Identificador", "Nome", "Tipo", "Preço", "Quantidade"))  # Exibe o cabeçalho do relatório de produtos
            for identificador, produto in estoque.items():                                                              # Percorre todos os produtos no estoque
                print("{:<14} {:<20} {:<15} R${:<9.2f} {:<10}".format(                                                  # Exibe as informações de cada produto formatadas
                    identificador, produto['nome'], produto['tipo'], produto['valor'], produto['quantidade']))          
        case 2:                                                                                                         # Caso a opção seja 2 (relatório de vendas realizadas)
            print("{:<10} {:<20} {:<10} {:<15}".format("Identificador", "Nome", "Quantidade", "Valor Total"))           # Exibe o cabeçalho do relatório de vendas
            for venda in vendas:                                                                                        # Percorre todas as vendas realizadas
                print("{:<14} {:<20} {:<10} R${:<9.2f}".format(                                                         # Exibe as informações de cada venda formatadas
                    venda['identificador_produto'], venda['nome_produto'],                                              
                    venda['quantidade_vendida'], venda['valor_total']))                                                 
        case _:                                                                                                         # Caso a opção seja diferente de 1 ou 2
            erro("Opção")                                                                                               # Exibe uma mensagem de erro para opção inválida 

while True:                             # Loop principal do programa                        
    titulo("MENU PRINCIPAL")            # Exibe o título do menu principal
    print("1 - Cadastrar Produto")      # Exibe a opção de cadastrar um produto
    print("2 - Alterar Produto")        # Exibe a opção de alterar um produto
    print("3 - Realizar Venda")         # Exibe a opção de realizar uma venda
    print("4 - Relatório de Produtos")  # Exibe a opção de gerar um relatório de produtos
    print("5 - Sair")                   # Exibe a opção de sair do programa

    opcao = input("Digite o número da opção desejada: ")    # Recebe a opção escolhida pelo usuário.
    opcao = func_verifica_numero(opcao, int)                # Verifica se a opção é um número válido.

    match opcao:                    # Verifica a opção selecionada
        case 1:                     # Caso a opção seja 1 (cadastrar produto)       
            cadastrar_produto()     # Chama a função para cadastrar um produto
        case 2:                     # Caso a opção seja 2 (alterar produto)
            alterar_produto()       # Chama a função para alterar um produto
        case 3:                     # Caso a opção seja 3 (realizar venda)
            realizar_venda()        # Chama a função para realizar uma venda
        case 4:                     # Caso a opção seja 4 (relatório de produtos)
            relatorio_produtos()    # Chama a função para gerar um relatório de produtos   
        case 5:                     # Caso a opção seja 5 (sair)                            
            break                   # Encerra o loop e finaliza o programa
        case _:                     # Caso a opção seja diferente de 1, 2, 3, 4 ou 5        
            erro("Opção")           # Exibe uma mensagem de erro para opção inválida

with open(banco_de_dados, 'w') as arquivo:                                  # Abre o arquivo de banco de dados em modo de escrita         
    json.dump({"estoque": estoque, "vendas": vendas}, arquivo, indent=2)    # Salva os dados do estoque e vendas no arquivo de banco de dados (JSON formatado)   
