class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.__preco = preco

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco = novo_preco
            print("Preço alterado com sucesso.")
        else:
            print("O preço deve ser maior que zero.")

    def mostrar_produto(self):
        print(f"Produto: {self.nome}")
        print(f"Preço: R$ {self.__preco:.2f}")


produto = Produto("Computador", 60)

produto.mostrar_produto()

produto.preco = 87
produto.mostrar_produto()

produto.preco = -20
produto.mostrar_produto()
