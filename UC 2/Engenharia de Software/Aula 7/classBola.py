class Bola():
    def __init__(self, cor, circunferência, material):
        self.cor = cor
        self.circunferência = circunferência
        self.material = material

    def trocar_cor(self):
        cor1 = "verde"
        cor2 = "azul"

        if self.cor == None:
            self.cor = cor1
            print(cor1)
        else:
            self.cor = cor2
            print(cor2)

    def mudar_cor():
        pass

    trocar_cor()