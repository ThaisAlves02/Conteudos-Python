from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, modelo, marca, ano, quantidade_portas):
        super().__init__(modelo, marca, ano)
        self.quantidade_portas = quantidade_portas
    
    def mostrar_portas(self):
        print(f"Qtd de portas: {self.quantidade_portas}")