class Produto:
    def __init__(self, nome, preco, estoque):
       self.nome = nome
       self.__preco = preco
       self.__estoque = estoque

    @property
    def preco(self):
        return self.__preco
    
    @preco.setter # O setter permite alterar o preço, mas antes verifica se o valor é válido.
    def preco(self, novo_preco):
        if novo_preco > 0 :
            self.__preco = novo_preco
        else:
            print("O preço deve ser maior que zero.")

    @property
    def estoque(self):
        return self.__estoque