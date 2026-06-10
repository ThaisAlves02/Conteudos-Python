while True:
    print("""
        MENU DE ATENDIMENTO
        1. Falar com um atendente
        2. Finalizar contrato
        3. Abrir nova conta
        4. Visualizar segunda via da fatura
        0. Sair
        
        
    """)
   
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        print("Aguarde alguns instantes, um de nossos atendentes entrará em contato com você.")
    elif opcao == "2":
        print("Daremos inicio a finalização do seu contrato.")
    elif opcao == "3":
        print("Para a abertura de conta os seguintes documentos são necessários: RG/CPF.")
    elif opcao == "4":
        print("A segunda via de sua fatura foi enviada agora para o seu email.")
    elif opcao == "0":
        print("Encerrando atendimento...")
        break
    else:
        print("Digite uma opção válida!")
        continue