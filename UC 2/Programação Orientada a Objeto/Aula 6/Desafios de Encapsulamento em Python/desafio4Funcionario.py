class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, novo_salario):
        if novo_salario > 0:
            self.__salario = novo_salario
        else:
            print("O salário deve ser maior que zero")
    
    def mostrar_salario(self):
        print(f"Funcionário: {self.nome}")
        print(f"Salário: {self.__salario}")
    
func1 = Funcionario("Luís", 1500)
func1.mostrar_salario()
