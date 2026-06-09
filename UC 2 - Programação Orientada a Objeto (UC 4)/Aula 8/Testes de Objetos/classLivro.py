class Livro():
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
    
    def mostrar_informacoes(self):
        print(f"""
INFORMAÇÕES DO LIVRO:
 Título:  {self.titulo}
 Autor: {self.autor}
 Ano: {self.ano}
""")
       