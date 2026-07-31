class Veiculo ():
    nome_estacionamento = "Shopping Central"
    valor_hora = 8.0 

    def __init__(self, placa, modelo, proprietario, horas_estacionadas):
       self.placa = placa
       self.modelo = modelo
       self.proprietario = proprietario
       self.horas_estacionadas = horas_estacionadas