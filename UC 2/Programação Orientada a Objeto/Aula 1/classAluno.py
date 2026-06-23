class Aluno:
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso
    
    def apresentar(self):
        print(f"Meu nome é {self.nome}, tenho {self.idade} anos e faço o curso de {self.curso}.")
        