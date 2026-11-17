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

    novo_nome = input(f"Novo nome: {nome_prod}").strip()

    if novo_nome:
        nome_prod = novo_nome

    novo_preco = input(f"Novo preço {preco_prod}: ").strip().replace(",", ".")
    if novo_preco:
        preco_prod = float(novo_preco)

    novo_estoque = input(f"Novo estoque {estoque_prod}: ").strip()
    if novo_estoque:
        estoque_prod = int(novo_estoque)

    nova_categoria = input(f"Nova categoria: {nome_ca}").strip()

    if nova_categoria:
        nome_ca = nova_categoria

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
            UPDATE produtos
            SET nome_produto = %s,
                preco = %s,
                estoque = %s,
                cod_categoria = %s
            WHERE cod_produto = %s;
        ''', (nome_prod, preco_prod, estoque_prod, id_categoria, cod))

        print("PRODUTO ATUALIZADO COM SUCESSO")
    except Exception as error:
        print(f"Falha na atualização: {error}")


def apagarProdutos():
    produtos = verDetalhes()

    if not produtos:
        return

    continuar = input("Deseja alterar as informações deste produto? (S/N): ").strip().upper()

    if continuar != "S":
        print("Operação cancelada.")
        return

    try:
        banco.manipular('''
            DELETE FROM itens_pedido
            WHERE cod_produto = %s;
        ''', (produtos[0],))

        banco.manipular('''
            DELETE FROM produtos
            WHERE cod_produto = %s;
        ''', (produtos[0],))

        print("\n[OK] Produto removido com sucesso!")
    except Exception as error:
        print(f"\n[ERRO] Não foi possível remover o produto: {error}")


while (True):
    print('''
          BEM VINDO A LOJA CONECTA
          
          MENU:
          
          1. Ver Produtos
          2. Ver Detalhes
          3. Cadastrar Produtos
          4. Alterar Produtos
          5. Apagar Produtos
          
          
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