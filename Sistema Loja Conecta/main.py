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
    

def verDetalhes():
    verProdutos()

    produtoescolhido = input(f"Digite o código do produto desejado: ")

    produtos = banco.consultar('''
    SELECT p.cod_produto, p.nome_produto, p.preco, p.estoque, c.nome_categoria FROM produtos p
    JOIN categorias c ON p.cod_categoria = c.cod_categoria
    WHERE p.cod_produto = %s;''', (produtoescolhido,))

    if len(produtos) == 0:
        print("PRODUTO NÃO ENCONTRADO")

    print(f"""
    FICHA DO PRODUTO
    CÓD. DO PRODUTO: {produtos[0][0]}
    NOME DO PRODUTO: {produtos[0][1]}
    PREÇO: {produtos[0][2]}
    ESTOQUE: {produtos[0][3]}
    CATEGORIA: {produtos[0][4]}
    """)
    
    return produtos[0]

def cadastrarProdutos():
    nome_prod = input("Digite o nome do produto: ").strip()
    preco_prod = float(input("Digite o preço do produto: "))
    estoque_prod = int(input("Digite o estoque do produto: "))
    nome_ca = input("Digite o nome da categoria: ").strip()

    try:
        categorias = banco.consultar('''
            SELECT cod_categoria FROM categorias WHERE nome_categoria ILIKE %s;
        ''', (nome_ca,))

        if not categorias:
            print(f"ERRO: A categoria '{nome_ca}' não foi encontrada!")
            id_categoria = None
        else:
            id_categoria = categorias[0][0]

        banco.manipular('''
            INSERT INTO produtos
            VALUES (default, %s, %s, %s, %s);
        ''', (nome_prod, preco_prod, estoque_prod, id_categoria))
        
        print("PRODUTO CADASTRADO COM SUCESSO!")
        
    except Exception as error:
        print(f"ERRO AO CADASTRAR PRODUTO! {error}")


def alterarProdutos():
    produtos = verDetalhes()

    if produtos is None:
        return

    continuar = input("Deseja alterar as informações deste produto? (S/N): ").strip().upper()

    if continuar != "S":
        print("Operação cancelada.")

    cod, nome_prod, preco_prod, estoque_prod, nome_ca = produtos

    print("Deixe em branco e tecle Enter para manter o valor atual: ")

    nome_prod = input(f"Novo nome: {nome_prod}")

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