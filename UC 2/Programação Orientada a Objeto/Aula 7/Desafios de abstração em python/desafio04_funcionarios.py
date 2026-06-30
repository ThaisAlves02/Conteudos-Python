from abc import ABC, abstractmethod


class Funcionario(ABC):
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    @abstractmethod
    def calcular_bonus(self):
        pass


class Gerente(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.20


class Vendedor(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.1


class Estagiario(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.05


funcionarios = [
    Gerente("João", 6000),
    Vendedor("Bruna", 4000),
    Estagiario("Maria", 1000)
]

for funcionario in funcionarios:
    bonus = funcionario.calcular_bonus()
    print(f"{funcionario.nome} receberá R$ {bonus:.2f} de bônus.")
