funcionarios = []

while True:
    print("------- Gerenciamento de funcionários -------")
    print("""
    --------- MENU DE OPÇÕES ----------
        1. Cadastro de funcionário
        2. Ver funcionário
        3. Ver detalhes de funcionário
        4. Sair
    """)
    
    op = input("Digite a opção desejada: ")

    if op == "1":
            nome = input("Digite o nome: ")
            idade = input("Digite a idade: ")
            salario = input("Digite o salário: ")
            cargo = input("Digite o cargo: ")

            while True:
                cpf = input("Digite o CPF com 11 caracteres: ")
                if len(cpf) != 11:
                    print("CPF inválido! O CPF deve conter somente 11 caracteres.")
                else:
                     break
                
            novo_func = {
                "Nome": nome,
                "Idade": idade,
                "CPF": cpf,
                "Salário": salario,
                "Cargo": cargo
            }
                    
            funcionarios.append(novo_func) 

    elif op == "2":
        contador = 1
        for f in funcionarios:
            print(f"{contador}. {f["Nome"]}")
            contador += 1

    elif op == "3":
        for f in funcionarios:
            print(f"{contador}. {f["Nome"]}")
            contador += 1

        numero = int(input("Digite o número do funciónario para saber mais detalhes (0 = Cancelar): "))
        if numero == 0:
             print("CANCELANDO OPERAÇÃO...")
        else:
            func_escolhido = funcionarios[numero]
            continue
    
        print(f"""
    FICHA DE FUNCIONÁRIO:
        Nome: {func_escolhido["Nome"]}
        Idade: {func_escolhido["Idade"]}
        CPF: {func_escolhido["CPF"]}
        Salário: {func_escolhido["Salário"]}
        Cargo: {func_escolhido["Cargo"]}
""")

    elif op.upper() == "4":
        break
    else:
         print("Digite uma opção válida!")

    input("Pressione enter para continuar")


