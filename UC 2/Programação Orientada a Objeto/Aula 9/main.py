from classCliente import Cliente

cliente1 = Cliente("Luíza", "02948349209", "85924356424", "ninguem@gmail.com")
cliente2 = Cliente("João", "12345678900", "85999999999", "joao@gmail.com")

cliente1.cadastrar_cliente()
cliente2.cadastrar_cliente()

for cliente in Cliente.novocliente:
    cliente.exibir_cliente()
