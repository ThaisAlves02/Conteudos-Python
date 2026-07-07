class Aluno():
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def exibir_informacoes(self):
        print(f"""
    FICHA DO ALUNO:
    Nome: {self.nome}
    Matrícula: {self.matricula}
              """)
        
    def situacao_aluno(self, notas):

        self.notas.extend(notas)
        media = sum(self.notas) / len(self.notas)

        if media >= 7 or media <= 10:
            print(f"""
        Situação: Aprovado!
        Média: {media:.1f}
                  """)
        elif media >= 3 and media <= 5:
            print(f"""
        Situação: Reprovado!
        Média: {media:.1f}
                  """)
