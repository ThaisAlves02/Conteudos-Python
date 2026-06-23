class Produto:
    def __init__(self, nome, preco, qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd
    
    def exibir_dados(self):
        print(f"""
        ESTOQUE DA LOJA:
        Nome: {self.nome}
        Preço: {self.preco}
        Quantidade: {self.qtd}
        """)

    def calcular_estoque(self):
        valorTotal = self.preco * self.qtd

        print(f"Total em estoque: R$ {valorTotal}")
