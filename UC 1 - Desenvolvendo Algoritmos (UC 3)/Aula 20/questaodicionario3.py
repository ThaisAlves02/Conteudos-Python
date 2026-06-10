agendaTelefonica = {
    "Julia": "8573920128",
    "Marcos": "8539103759",
    "Miguel": "8532450135",
    "Letícia": "8529175838",
    "Amanda": "8529195738",
    "Rafael": "8529375928",
    "Bruno": "85298572974",
    "Bianca": "8529481938",
    "Natiele": "8520184769",
    "Pedro": "8529174301"
}


for i in range(5):
    nome = input("Digite o nome da pessoa: ")
    telefone = input("Digite o seu telefone: ")
    agendaTelefonica[nome] = telefone


while True: 
    nome = input("Digite o nome do contato que você deseja ver: ")

    if nome.upper() == "SAIR":
        print("Encerrando o app agenda...")
        break

    print(agendaTelefonica.get(nome, "Nome não encontrado!"))

    # if nome in agendaTelefonica:
    #      print(agendaTelefonica[nome])
    # else:
    #      print("Nome não encontrado!")


    



    




