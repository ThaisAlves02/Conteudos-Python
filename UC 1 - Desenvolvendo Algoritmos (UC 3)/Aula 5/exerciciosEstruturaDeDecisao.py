# =========== EXERCÍCIO 1 ===========
# Crie um programa que recebe a idade de uma pessoa e imprime na tela "Seu acesso está liberado" quando ela for maior de idade e "Acesso Negado" quando ela for menor de idade.

# =========== SOLUÇÃO ===========
idade = int(input("Digite sua idade:"))

if idade >= 18:
     print("Seu acesso está liberado")
     print("Você é maior de idade")
else:
     print("Acesso negado")
     print("Você é menor de idade")

print("Boa noite!")


# =========== EXERCÍCIO 2 ===========
# Crie um programa que pergunta o turno atual (Dia/Noite). Se o turno for Dia, imprima na tela "Bom dia!", se não imprima na tela "Boa noite!"

#Melhore o programa para incluir o turno da Tarde

# =========== SOLUÇÃO ===========
turnoAtual = input("Digite o seu turno (Dia/Tarde/Noite):")

if turnoAtual == "Dia" or turnoAtual == "dia":
    print("Bom dia!")
elif turnoAtual == "Tarde":
    print("Boa Tarde!")
elif turnoAtual == "Noite":
    print("Boa Noite!")
else:
    print("Digite um turno válido!")