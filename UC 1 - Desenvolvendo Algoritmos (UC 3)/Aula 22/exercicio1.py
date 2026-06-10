paciente = []

while True:
    nome = input("Digite o nome do paciente: ")

    if nome.upper() == "SAIR":
        print("Encerrando o cadastro de pacientes...")
        break

    idade = int(input("Digite a idade do paciente: "))
    genero = input("Digite o gênero do paciente: ")
    peso = float(input("Digite o peso do paciente: "))

    novoPaciente = {
        "Nome": nome,
        "Idade": idade,
        "Gênero": genero,
        "Peso": peso
    }

    paciente.append(novoPaciente)


print("Lista de Pacientes")

contador = 1
qtdAcima30 = 0
qtdAbaixo30 = 0

for p in paciente:
        print(f"{contador}. ")
        contador += 1

        if paciente["Idade"] > 30:
             qtdAcima30 += 1
        else:
             qtdAbaixo30 += 1

print(f"""
Total Acima de 30: {qtdAcima30} 

Total Abaixo de 30: {qtdAbaixo30} 
""")