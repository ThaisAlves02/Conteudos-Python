class Aluno ():
    def __init__(self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas
    
    def mostrar_informacoes(self):
        print(f"""
FICHA DO ALUNO:
 Nome:  {self.nome}
 Idade: {self.idade}
 Notas: {self.notas}
""")
        
        