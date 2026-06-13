#Revisão 2: Faça um programa de cadastro de funcionário onde são pedidos 5 informações de um funcionário (você escolhe as informações). Uma informação deve ser número decimal(float) e outra informação deverá ser o ano de nascimento. Ao final imprima a ficha do funcionário incluindo sua idade (sugestão use multi-linha)

print("RH Soluções XYZ")
print()
print("Cadastro de Funcionários")

nome_Func = input("Digite seu nome:")
ano_nascimento = int(input("Digite o ano do seu nascimento: "))
salario = float(input("Digite o seu salário:"))
cargo =input("Digite o seu cargo:")
setor =input("Digite o seu setor:")

idade = 2026 - ano_nascimento

print(f"""
Ficha do funcionário
      Nome:{nome_Func}
      Idade:{idade}
      Salário:R$ {salario:,.2f}
      Cargo:{cargo}
      Setor:{setor}
""")