class Livro():
    def __init__(self, titulo, autor):
       self.titulo = titulo
       self.autor = autor
       self.notasReputacao = []

    def detalhes(self):
        print(f"""
=== DETALHES DO LIVRO ===
Título: {self.titulo}
Autor: {self.autor}
""")
    
    def reputacao_livro(self, nota):
        self.notasReputacao.append(nota)
        mediaReputacao = sum(self.notasReputacao) / len(self.notasReputacao)

        if mediaReputacao >= 4.5:
            print(f"Excelente - Média: {mediaReputacao:.2f}")
        elif mediaReputacao >= 3.5:
            print(f"Boa - Média: {mediaReputacao:.2f}")
        else:
            print(f"Regular - Média: {mediaReputacao:.2f}")