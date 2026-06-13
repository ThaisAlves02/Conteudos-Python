class Pokemon ():
    def __init__(self, nome, ataque, defesa):
        self.nome = nome
        self.ataque = ataque
        self.defesa = defesa
    
    def mostrar_informacoes(self):
        print(f"""
    INFORMAÇÕES DO POKÉMON
    Nome: {self.nome}
    Ataque: {self.ataque}
    Defesa: {self.defesa}
""")