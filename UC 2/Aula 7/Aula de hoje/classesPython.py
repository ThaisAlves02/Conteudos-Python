class Pessoa :
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self, nome, idade,ano):
        super().__init__(nome, idade)
        self.ano = ano

class Professor(Aluno):
    def __init__(self, nome, idade, ano):
        super().__init__(nome, idade, ano)

class Veiculo:
    def __init__(self, modelo, marca, ano):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
    
    def apresentar(self):
        print("==== DADOS DO VEÍCULO ====")
        print(f"""
        Modelo: {self.modelo}
        Marca: {self.marca}
        Ano: {self.ano}
             """)
        
class Carro(Veiculo):
    def __init__(self, modelo, marca, ano, quantidade_portas):
        super().__init__(modelo, marca, ano)
        self.quantidade_portas = quantidade_portas
    
    def mostrar_portas(self):
        print(f"Qtd de portas: {self.quantidade_portas}")

class Moto(Veiculo):
    def __init__(self, modelo, marca, ano, cilindradas):
        super().__init__(modelo, marca, ano)
        self.cilindradas = cilindradas
    
    def mostrar_cilindradas(self):
        print(f"Cilindradas: {self.cilindradas}")
