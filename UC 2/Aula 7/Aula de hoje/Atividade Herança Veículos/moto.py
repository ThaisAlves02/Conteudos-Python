from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, modelo, marca, ano, cilindradas):
        super().__init__(modelo, marca, ano)
        self.cilindradas = cilindradas
    
    def mostrar_cilindradas(self):
        print(f"Cilindradas: {self.cilindradas}")
