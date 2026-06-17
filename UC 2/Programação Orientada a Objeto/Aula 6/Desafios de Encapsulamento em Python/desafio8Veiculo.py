class Veiculo:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.__ano = ano

    @property
    def ano(self):
        return self.__ano
    @ano.setter
    def ano(self, novo_ano):
        if novo_ano >= 1900:
            self.__ano = novo_ano
            print("Ano alterado com sucesso.")
        else:
            print("Ano inválido.")

    def mostrar_veiculo(self):
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.__ano}")


veiculo = Veiculo("Chevrolet", 2020)

veiculo.mostrar_veiculo()

veiculo.ano = 2023
veiculo.mostrar_veiculo()

veiculo.ano = 1856
veiculo.mostrar_veiculo()
