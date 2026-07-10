from classSalaodeBeleza import Cliente, Servico, Agendamento

clientes = []
servicos = []
agendamentos = []

def cadastrar_cliente():
    print("=== CADASTRO DE CLIENTES ===")

    while True:
        nome = input("Nome: ")
        if nome == "":
            print("O campo nome está vazio, digite um nome!")
            continue
        else:
            break
    
    cliente_existente = False
    for nome_cliente in clientes:
        if nome_cliente.nome == nome:
            cliente_existente = True
            break

    if cliente_existente:
        print(f"O Cliente {nome} já está cadastrado!")

    while True:
        cpf = input("CPF: ")
        if cpf == "":
            print("O campo CPF está vazio, digite um CPF!")
            continue
        else:
            break

    cpf_existe = False
    for cliente in clientes:
        if cliente.cpf == cpf:
             cpf_existe = True
             break
        
    if cpf_existe:
                print(f"O CPF {cpf} já está cadastrado!")
    else:
        telefone = input("Telefone: ")
        email = input("E-mail: ")

        cliente = Cliente(nome, cpf, telefone, email)
        clientes.append(cliente)

        print()
        print("Cliente cadastrado com sucesso!")                
    

def cadastrar_servico():
    print("=== CADASTRO DE SERVIÇOS ===")

    nome = input("Nome: ")
    
    servico_existente = False
    for nome_servico in servicos:
        if nome_servico.nome == nome:
            servico_existente = True
            break
    
    if servico_existente:
        print(f"O serviço {nome} ja esta cadastrado")
    else:
        while True:
            valor = float(input("Valor: "))
            if valor > 0:
                break
            print("O valor deve ser maior que zero.")

        duracao = int(input("Duração (minutos): "))

        servico = Servico(nome, valor, duracao)
        servicos.append(servico)

    
def exibir_cliente():
    print("VIZUALIZAR CLIENTES")
         
    if not clientes:
        print("Nenhum cliente cadastrado.")
        
    for i, cliente in enumerate(clientes):
        print(f"{i+1} - {cliente.nome}")


def exibir_servico():
    if not servicos:
       print("Nenhum serviço cadastrado.")
    
    for i, servico in enumerate(servicos):
        print(f"{i+1} - {servico.nome}")


def agendar():
    print("=== AGENDAR ATENDIMENTO ===")

    if len(clientes) == 0:
        print("Cadastre um cliente primeiro.")
      
    if len(servicos) == 0:
        print("Cadastre um serviço primeiro.")

    exibir_cliente()

    num_cliente = int(input("Digite o número do cliente: "))

    if num_cliente < 1 or num_cliente > len(clientes):
        print("Cliente inválido!")
    
    exibir_servico()

    num_servico = int(input("Digite o número do serviço: "))

    if num_servico < 1 or num_servico > len(servicos):
        print("Serviço inválido!")

    data = input("Data (dd/mm/aaaa): ")
    horario = input("Horário (HH:MM): ")

    for agenda in agendamentos:
        if agenda.data == data and agenda.horario == horario:
            print("Já existe um agendamento nesse horário!")
    
    novoAgn = Agendamento(
        clientes[num_cliente-1],
        servicos[num_servico-1],
        data,
        horario
    )

    agendamentos.append(novoAgn)


def exibir_agendamento():
    print(f"VIZUALIZAR AGENDAMENTOS")

    if not agendamentos:
        print("Nenhum agendamento.")

    for i, agn in enumerate(agendamentos):
        print(f"{i+1} - Cliente: {agn.cliente.nome} | Serviço: {agn.servico.nome} | Data: {agn.data} | Horário: {agn.horario}")


def editar_cliente():
    exibir_cliente()

    num_cliente = int(input("Digite o número do cliente que deseja remover: "))

    cliente_escolhido = clientes[num_cliente-1]

    novo_nome = input("Escreva o novo nome: ")
    if novo_nome:
        cliente_escolhido.nome = novo_nome
    
    novo_telefone = input("Escreva o novo telefone: ")
    if novo_telefone:
        cliente_escolhido.telefone = novo_telefone
    
    novo_email = input("Escreva o novo email: ")
    if novo_email:
        cliente_escolhido.email = novo_email


def editar_agendamento():
    exibir_agendamento()
    
    num_agendamento = int(input("Digite o número do agendamento: "))

    agendamento_escolhido = agendamentos[num_agendamento - 1]

    novo_servico = input("Digite um novo serviço: ")
    if novo_servico:
      agendamento_escolhido.servico.nome = novo_servico

    novo_horario = input("Digite um novo horário: ")
    if novo_horario:
        agendamento_escolhido.horario = novo_horario
    
    nova_data = input("Digite uma nova data: ")
    if nova_data:
        agendamento_escolhido.data = nova_data



def cancelar_agendamento():
    print("\n=== Cancelar Agendamento ===")

    if not agendamentos:
        print("Nenhum agendamento cadastrado.\n")
        return

    exibir_agendamento()

    num = int(input("Digite o número do agendamento: "))
    num -=1
    
    if 0 <= num < len(agendamentos):
        agendamentos.pop(num)
        print("Agendamento cancelado!")
    else:
        print("Número inválido.")


while True:

    print("""======== SALÃO DE BELEZA ========
            1 - Cadastrar Cliente
            2 - Cadastrar Serviço
            3 - Agendar Atendimento
            4 - Listar serviços
            5 - Listar Agendamentos
            6 - Editar cliente
            7 - Editar agendamento
            8 - Cancelar Agendamento
          
            0 - Sair
                """)

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_cliente()

    elif opcao == "2":
        cadastrar_servico()

    elif opcao == "3":
        agendar()

    elif opcao == "4":
        exibir_servico()
    
    elif opcao == "5":
        exibir_agendamento()

    elif opcao == "6":
        editar_cliente()

    elif opcao == "7":
        editar_agendamento()

    elif opcao == "8":
        cancelar_agendamento()

    elif opcao == "0":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida.")