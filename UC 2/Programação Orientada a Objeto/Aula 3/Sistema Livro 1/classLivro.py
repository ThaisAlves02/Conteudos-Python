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

        # É possível usar if-else e outras estruturas dentro do comando de criação

        # if autor == "Machado de Assis":   
        #     self.ano = 1800
        # elif autor == "Tolkien":
        #     self.ano = 1947
        # else:
        #     self.ano = 2026

    def mostrar_informacoes(self):

        print(f"""
INFORMAÇÕES DO LIVRO
              
    TITULO: {self.titulo.title()}
    AUTOR: {self.autor.title()}
    GÊNERO: {self.genero.title()}

""")