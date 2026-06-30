from abc import ABC, abstractmethod


class Produto(ABC):
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    @abstractmethod
    def calcular_preco_final(self):
        pass


class ProdutoFisico(Produto):
    def calcular_preco_final(self):
        return self.preco + (self.preco *0.1)


class ProdutoDigital(Produto):
    def calcular_preco_final(self):
        return self.preco


class Servico(Produto):
    def calcular_preco_final(self):
        return self.preco + (self.preco * 0.15)


produtos = [
    ProdutoFisico("Computador", 4500),
    ProdutoDigital("Cursos EAD", 100),
    Servico("Instalação de jogos", 600)
]

for produto in produtos:
    preco_final = produto.calcular_preco_final()
    print(f"{produto.nome}: R$ {preco_final:.2f}")
