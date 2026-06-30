from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    @abstractmethod
    def calcular_tarifa(self):
        pass


class ContaCorrente(Conta):
    def calcular_tarifa(self):
        return 25


class ContaPoupanca(Conta):
    def calcular_tarifa(self):
        return 20


class ContaEmpresarial(Conta):
    def calcular_tarifa(self):
        return 100


contas = [
    ContaCorrente("Júlia", 2400),
    ContaPoupanca("Renato", 700),
    ContaEmpresarial("Empresa do seu Zé", 7000)
]

for conta in contas:
    tarifa = conta.calcular_tarifa()
    print(f"Titular: {conta.titular} - Tarifa: R$ {tarifa:.2f}")
