class Cliente():
    novocliente = []

    def __init__(self, nome, cpf, telefone, email):
       self.nome = nome
       self.cpf = cpf
       self.telefone = telefone
       self.email = email
       
    
    def cadastrar_cliente(self):
        Cliente.novocliente.append(self)
    
    def exibir_cliente(self):
         print(f"""
    Nome: {self.nome}
    CPF: {self.cpf}
    Telefone: {self.telefone}
    Email: {self.email}
    """)
