class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            print(f"TITULAR DA CONTA: {self.titular} ")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
            self.__saldo += valor
        else:
            print("O valor do depósito deve ser maior que zero.")

    def sacar(self, valor):
        if valor <= 0:
            print("O valor do saque deve ser maior que zero.")

        elif valor <= self.__saldo:
            self.__saldo -= valor 
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

        else:
            print("Saldo insuficiente.")


    def mostrar_saldo(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo atual: R$ {self.__saldo:.2f}")


    def saldo_bancario(self):
        print(f"Saldo atual: {self.__saldo:.2f}")



conta1 = ContaBancaria("Ana", 100)
conta1.saldo_bancario()
conta1.titular = "ZÉ DOIDIM"
conta1.depositar(50)
conta1.saldo_bancario()

conta1.sacar(200)
conta1.saldo_bancario()

conta1.sacar(80)
conta1.__saldo = -1000
conta1.saldo_bancario()

