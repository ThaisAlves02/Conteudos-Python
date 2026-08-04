class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
          self._saldo += valor
          print(f"{valor:.2f}")

    def sacar(self, valor):
        if valor <= 0:
            print(f"O valor do saque deve ser maior que zero.")
        elif valor > 0:
            self._saldo -= valor
            print(f"")
