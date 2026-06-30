from abc import ABC, abstractmethod


class Entrega(ABC):
    @abstractmethod
    def calcular_frete(self, peso, distancia):
        pass


class EntregaLocal(Entrega):
    def calcular_frete(self, peso, distancia):
        return peso * 2 * distancia


class EntregaNacional(Entrega):
    def calcular_frete(self, peso, distancia):
        return peso * distancia * 0.05


class RetiradaLoja(Entrega):
    def calcular_frete(self, peso, distancia):
        return peso * distancia


entregas = [
    EntregaLocal(),
    EntregaNacional(),
    RetiradaLoja()
]

for entrega in entregas:
    frete = entrega.calcular_frete(5, 10)
    print(f"Frete: R$ {frete:.2f}")
