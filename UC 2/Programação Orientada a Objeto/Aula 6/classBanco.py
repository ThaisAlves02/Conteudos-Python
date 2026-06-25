class Banco():
    def __init__(self, cliente, saldo, senha, status = False):
        self.cliente = cliente
        self.__saldo = saldo
        self.__senha = senha
        self.status = status

    def fazer_login(self):
        while True:
            senha = input("Digite sua senha: ")
            if senha == self.__senha:
                print("Senha correta, acesso liberado.")
                self.status = True
                break
            else:
                print("Senha incorreta. Tente novamente!")
                self.status = False

    def exibir_conta(self):
        if self.status:
            print(f"""
=== EXTRATO DA CONTA ===
    Cliente: {self.cliente}
    Saldo: R$ {self.__saldo:,.2f}
""")
        else:
            print("Para ver sua conta, digite primeiro sua senha.")

if __name__ == "__main__":

    pessoa1 = Banco("Pedro", 1500, "pedrolindo")

    pessoa1.exibir_conta()
    pessoa1.fazer_login()
    pessoa1.exibir_conta()