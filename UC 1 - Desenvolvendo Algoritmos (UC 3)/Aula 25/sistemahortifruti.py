# 6 — 🌱 Estoque de Hortifruti
# Atributos: produto, unidade (kg/unidade), quantidade em estoque, preço, fornecedor

# Funcionalidade extra: alertar quais produtos estão abaixo de uma quantidade mínima informada pelo usuário

produtos = [
    {
        "Nome": "Tomate",
        "Preço": 8.50,
        "Estoque": 120,
        "Unidade": "kg",
        "Fornecedor": "Verde Vida Hortifruti"
    },
    {
        "Nome": "Banana Prata",
        "Preço": 5.99,
        "Estoque": 200,
        "Unidade": "kg",
        "Fornecedor": "Frutas do Vale"
    },
    {
        "Nome": "Alface Americana",
        "Preço": 3.50,
        "Estoque": 80,
        "Unidade": "un",
        "Fornecedor": "Horta Natural"
    },
    {
        "Nome": "Batata Inglesa",
        "Preço": 6.75,
        "Estoque": 150,
        "Unidade": "kg",
        "Fornecedor": "Campo Fresco"
    },
    {
        "Nome": "Cenoura",
        "Preço": 4.20,
        "Estoque": 100,
        "Unidade": "kg",
        "Fornecedor": "Raízes da Terra"
    },
    {
        "Nome": "Maçã Gala",
        "Preço": 9.90,
        "Estoque": 90,
        "Unidade": "kg",
        "Fornecedor": "Pomar Central"
    },
    {
        "Nome": "Cebola",
        "Preço": 7.30,
        "Estoque": 130,
        "Unidade": "kg",
        "Fornecedor": "Sabor do Campo"
    },
    {
        "Nome": "Mamão Formosa",
        "Preço": 6.10,
        "Estoque": 60,
        "Unidade": "kg",
        "Fornecedor": "Frutas Tropicais"
    },
    {
        "Nome": "Cheiro Verde",
        "Preço": 2.80,
        "Estoque": 70,
        "Unidade": "molho",
        "Fornecedor": "Horta Feliz"
    },
    {
        "Nome": "Laranja Pera",
        "Preço": 4.99,
        "Estoque": 180,
        "Unidade": "kg",
        "Fornecedor": "Citrus Brasil"
    }
]

while True:
    print("BEM VINDO AO SISTEMA DE GERENCIAMENTO HORTIFRUTI SEU PEREIRA")

    print(f"""

MENU DE OPÇÕES:
          
    1. Cadastrar um produto
    2. Ver lista de produtos
    3. Ver produto específico
    4. Ver produtos pelo estoque mínimo
    5. Ver produtos pelo preço
    6. Venda de produtos

    0. Sair 
""")
    op = input("Digite a opção desejada: ")
    

    if op == "1":

        print()
        print("CADASTRO DE PRODUTO")
        print()

        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        unidade = input("Digite o tipo de unidade (kg/und): ")
        estoque = int(input("Digite a quantidade do produto: "))
        fornecedor = input("Digite o fornecedor: ")

        novo_produto = {
            "Nome": nome,
            "Preço": preco,
            "Estoque": estoque,
            "Unidade": unidade,
            "Fornecedor": fornecedor
        }

        produtos.append(novo_produto)
        print()
        print("PRODUTO CADASTRADO COM SUCESSO")
        print(f"Produtos no Catálogo: {len(produtos)}")

        
    elif op == "2":
        print()
        print("VER PRODUTOS")
        print()
        contador = 1
        for i,produto in enumerate(produtos):
            print(f"{contador}. {produto["Nome"]} | {produto["Estoque"]}")
            contador += 1

    elif op == "3":
        print()
        print("ESCOLHER PRODUTO")
        print()
        
        contador = 1
        for produto in produtos:
            print(f"{contador}. {produto["Nome"]} | {produto["Estoque"]}")
            contador += 1

        print()
        numero = int(input("Digite o número do produto que deseja visualizar: "))
        if numero == 0:
            print("CANCELANDO OPERAÇÃO")
        elif numero >= 1 and numero <= len(produtos):

            produto_escolhido = produtos[numero-1]

            print(f"""
    INFORMAÇÕES DO PRODUTO
        
        Nome: {produto_escolhido["Nome"]}
        Preço: R$ {produto_escolhido["Preço"]:,.2f}
        Estoque: {produto_escolhido["Estoque"]} {produto_escolhido["Unidade"]} 
        Fornecedor: {produto_escolhido["Fornecedor"]}

    """)
        else:
            print("DIGITE UM NÚMERO VÁLIDO")
        
    elif op == "4":
        print()
        print("VER PRODUTOS POR ESTOQUE")
        print()

        estoque_minimo = int(input("Digite o estoque mínimo: "))

        print("Nº | Nome | Estoque | Unidade")
        for i, produto in enumerate(produtos):
            if produto["Estoque"] <= estoque_minimo:
                print(f"{i+1} | {produto["Nome"]} | {produto["Estoque"]} | {produto["Unidade"]}")

    # Criar a funcionalidade 5, pesquisar pelo preço. O programa deve exibir todos os produtos que tem o preço maior ou igual ao preço digitado pelo usuário!
    elif op == "5":
        print()
        print("VER PRODUTOS PELO PREÇO")
        print()

        pesquisa_preco = float(input("Digite o preço do produto que deseja ver: "))

        for i, produto in enumerate(produtos):
            if produto["Preço"] >= pesquisa_preco:
                print(f"{i+1} | {produto["Nome"]} | R$ {produto["Preço"]:,.2f}")
    
    elif op == "6":
        print()
        print("VENDA DE PRODUTO")
        print()
        
       
        for i, produto in enumerate(produtos):
            print(f"{i+1}. {produto["Nome"]} | {produto["Estoque"]}")
            

        produto_vendido = int(input("Digite o número do produto que você deseja: "))
        qtd_vendida = int(input("Digite a quantidade que deseja: "))

        if produto_vendido == 0:
            print("CANCELANDO OPERAÇÃO")

        elif produto_vendido >= 1 and produto_vendido <= len(produtos):

            produto_escolhido = produtos[produto_vendido-1]

            if qtd_vendida <= len(produtos):
                total = produto_escolhido["Preço"] * qtd_vendida
                produto_escolhido["Estoque"] -= qtd_vendida
                
                print(f"""
        RESUMO DA VENDA
        Produto: {produto_escolhido["Nome"]}
        Preço unitário: R$ {produto_escolhido["Preço"]:,.2f}
        Qtd comprada: {qtd_vendida}
        Total: {total}
    """)

    elif op == "0":
        print("ENCERRANDO PROGRAMA...")
        break
    else:
        print("DIGITE UMA OPÇÃO VÁLIDA")

    
    input("DIGITE ENTER PARA CONTINUAR...")