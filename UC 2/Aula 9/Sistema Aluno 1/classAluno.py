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
        
        print("SITUAÇÃO:")
        self.calcular_situacao()
        
    def calcular_media(self):
        media = sum(self.notas)/len(self.notas)
        return media
    
    def calcular_situacao(self):

        media = self.calcular_media()

        if media >= 7 and media <=10:
            print("APROVADO!")
        elif media >= 4 and media < 7:
            print("RECUPERAÇÃO!")
        elif media >= 0 and media < 4:
            print("REPROVADO")
        else:
            print("MÉDIA INVÁLIDA!")