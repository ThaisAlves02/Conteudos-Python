from classVeiculo import Veiculo

def adicionar_horas(self):
        hora_adicionada = int(input("Digite a quantidade de horas estacionadas: "))

        self.horas_estacionadas = self.horas_estacionadas + hora_adicionada

        print(f"HORAS: {self.horas_estacionadas}")


def calcular_valor_total(self):
       total = self.horas_estacionadas * self.valor_hora

       print(f"Valor total: {total}")


def exibir_dados(self):
        print(f"""
    == DADOS DO VEÍCULO ==
    Placa: {self.placa}
    Modelo: {self.modelo}
    Proprietário: {self.proprietario}
    Horas Estacionadas: {self.horas_estacionadas}
    """)
