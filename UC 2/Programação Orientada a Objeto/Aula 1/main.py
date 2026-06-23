from classFuncionario import Funcionario

from classProduto import Produto

from classAluno import Aluno

# CLASSE FUNCIONÁRIO
func_1 = Funcionario("João", 5000, 25, "Vendedor")

func_2 = Funcionario("Maria", 7000, 35, "Gerente")

print(func_2.nome)
func_1.exibir_dados()
func_2.calcular_salario_anual()

# CLASSE PRODUTO
produto1 = Produto("caderno", 10, 4)

produto1.exibir_dados()

produto1.calcular_estoque()
print()

# CLASSE ALUNO
aluno1 = Aluno("Júlia", 20, "Culinária")
aluno1.apresentar()