class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo
    
    @property
    def saldo(self):
        return self.__saldo
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    def mostrar_conta(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo: R$ {self.__saldo:.2f}")


conta = ContaBancaria("Bruna", 1000)

conta.mostrar_conta()

conta.depositar(300)
conta.sacar(100)

print(conta.saldo)

conta.sacar(200)
conta.mostrar_conta()