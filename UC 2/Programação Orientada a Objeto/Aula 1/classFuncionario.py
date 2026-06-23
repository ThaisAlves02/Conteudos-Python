class Funcionario:
    # Método Construtor - Cria o objeto
    def __init__(self, nome, salario, idade, cargo):
        self.nome = nome
        self.salario = salario
        self.idade = idade
        self.cargo = cargo
    
    def exibir_dados(self):
        print(f"""
        FICHA DO FUNCIONÁRIO:
        Nome: {self.nome}
        Salário: {self.salario}
        Idade: {self.idade}
        Cargo: {self.cargo}
        """)
    
    def calcular_salario_anual(self):
        salario = self.salario * 12
        print(f"Salário Anual: R$ {salario}")