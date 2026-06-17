# Criar uma classe Pessoa com nome público e idade privada.

# A idade só poderá ser alterada se for maior ou igual a zero.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.__idade = idade
    
    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, nova_idade):
      if nova_idade >= 0:
            self.__idade = nova_idade
      else:
          print("A idade não pode ser negativa.")
        
    
    def apresentar(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.__idade}")

pessoa = Pessoa("Júlia", 30)

pessoa.apresentar()

pessoa.idade = 23
pessoa.apresentar()

pessoa.idade = -6
pessoa.apresentar()