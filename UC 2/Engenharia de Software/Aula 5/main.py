from classProdutos import Produtos

produtos = [
    Produtos(id = 1, nome = "Notebook", estoque = 15),
    Produtos(id = 2, nome = "Mouse", estoque = 50),
    Produtos(id = 3, nome = "Teclado", estoque = 30),
    Produtos(id = 4, nome = "Monitor", estoque = 12),
    Produtos(id = 5, nome = "Headset", estoque = 20),
]


def consultar_produtos():
    print("CONSULTAR PRODUTOS")
    print()

    for i, produto in enumerate(produtos):
        print(f"{i+1} - {produto.nome}")

    print()
    produto_escolhido = int(input("Digite o número do produto para ver mais detalhes: "))

    if produto_escolhido >= 1 and produto_escolhido <= len(produtos):
        produto = produtos[produto_escolhido - 1]
        print(f"{produto.id} - {produto.nome} - {produto.estoque}")

consultar_produtos()
