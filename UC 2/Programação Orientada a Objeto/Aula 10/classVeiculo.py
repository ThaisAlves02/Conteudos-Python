class Veiculo():
    nome_estacionamento = "Shopping Central"
    valor_hora = 8.0 

    def __init__(self, placa, modelo, proprietario, horas_estacionadas):
       self.placa = placa
       self.modelo = modelo
       self.proprietario = proprietario
       self.horas_estacionadas = horas_estacionadas

    def adicionar_horas(self):
        
            hora_adicionada = int(input("Digite a quantidade de horas estacionadas: "))

            self.horas_estacionadas = self.horas_estacionadas + hora_adicionada

            print(f"HORAS: {self.horas_estacionadas}")


    def calcular_valor_total(self):
        total = self.horas_estacionadas * self.valor_hora

        print(f"Valor total: {total:.2f}")


    def exibir_dados(self):
            print(f"""
        == DADOS DO VEÍCULO ==
        Placa: {self.placa}
        Modelo: {self.modelo}
        Proprietário: {self.proprietario}
        Horas Estacionadas: {self.horas_estacionadas}
        """)
