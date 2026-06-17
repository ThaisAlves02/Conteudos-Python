class Livro:
    def __init__(self, titulo, preco):
        self.titulo = titulo
        self.__preco = preco

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco = novo_preco
            print("Preço do livro atualizado.")
        else:
            print("O preço do livro deve ser maior que zero.")

    def mostrar_livro(self):
        print(f"Livro: {self.titulo}")
        print(f"Preço: R$ {self.__preco:.2f}")


livro = Livro("DOM CASMURRO", 67.90)

livro.mostrar_livro()

livro.preco = 79.90
livro.mostrar_livro()

livro.preco = 0
livro.mostrar_livro()
