class Estoque:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.__quantidade = quantidade

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, nova_quantidade):
        if nova_quantidade >= 0:
            self.__quantidade = nova_quantidade
            print("Quantidade atualizada com sucesso.")
        else:
            print("A quantidade não pode ser negativa.")

    def mostrar_estoque(self):
        print(f"Produto: {self.produto}")
        print(f"Quantidade em estoque: {self.__quantidade}")


estoque = Estoque("Mouse", 20)

estoque.quantidade = 6
estoque.mostrar_estoque()

estoque.quantidade = -2
estoque.mostrar_estoque()
