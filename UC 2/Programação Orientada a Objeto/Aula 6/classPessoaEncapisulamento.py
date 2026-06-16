# Atributo Público
class Pessoa:
    def __init__(self, nome):
        self.nome = nome


pessoa1 = Pessoa("Ana")
print(pessoa1.nome)


# Atributo Privado

class Pessoa:
    def __init__(self, nome):
       self.__nome = nome

    @property
    def nome (self):
       return self.__nome

pessoa1 = Pessoa("Ana")
pessoa1.__nome = "ANDRÉ"

print(pessoa1.nome)

