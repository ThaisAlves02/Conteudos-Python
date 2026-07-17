class Aluno():
    escola = "Senac"
    qtd_alunos = 0

    def __init__(self, nome):
        self.nome = nome
        Aluno.qtd_alunos += 1

aluno1 = Aluno("João")
aluno2 = Aluno("André")

print(aluno1.nome)
print(aluno2.nome)

print(f"Escola: {Aluno.escola}")
print(f"Quantidade de alunos: {Aluno.qtd_alunos}")