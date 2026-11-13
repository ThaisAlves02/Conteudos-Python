from classBanco import Banco

banco = Banco()

def verProdutos():
    print("LISTA DE PRODUTOS")

    produtos = banco.consultar('''
    SELECT p.cod_produto, p.nome_produto, p.preco, p.estoque, c.nome_categoria FROM produtos p
    JOIN categorias c ON p.cod_categoria = c.cod_categoria
    ORDER BY p.cod_produto ASC;
''')
    
    if (len(produtos) == 0):
            print("NÃO HÁ PRODUTOS CADASTRADOS")

    print("CÓDIGO | NOME | PREÇO | ESTOQUE | CATEGORIA")
    for cod_prod, nome_prod, preco_prod, estoque_prod, nome_ca in produtos:
        print(f"{cod_prod} | {nome_prod} | {preco_prod} | {estoque_prod} | {nome_ca}")
    



while (True):
    print('''
          BEM VINDO A LOJA CONECTA
          
          MENU:
          
          1. Ver Produtos
          2. Ver Detalhes
          3. Cadastrar Produtos
          4. Alterar
          5. Apagar
          
          
          0. Sair
          ''')
    
    op = input("DIGITE O NÚMERO DA OPÇÃO DESEJADA:")
    
    if (op == "1"):
        verProdutos()
    elif (op == "2"):
        verDetalhes()
    elif (op == "3"):
        cadastrarProdutos()
    elif (op == "4"):
        alterarProdutos()
    elif (op == "5"):
        apagarProdutos()
    elif (op == "0"):
        print("Saindo do programa...")
        break
    else:
        print("ESCOLHA UMA OPÇÃO VÁLIDA")
    
    input("TECLE ENTER PARA CONTINUAR")