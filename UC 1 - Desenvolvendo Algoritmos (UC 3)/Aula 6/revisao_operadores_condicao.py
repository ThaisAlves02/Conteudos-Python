# =========== EXERCÍCIO 1 ===========
# Crie um programa que pergunta se uma pessoa tem reserva para o restaurante. Verifique se a resposta foi especificamente "Sim" e imprima o resultado da verificação:

#Ex: "Entrada Permitida: {True/False}"

# =========== SOLUÇÃO ===========
reserva = input("Você tem reserva?")

resposta = reserva == "Sim"

print(f"Entrada permitida: {resposta}")


# =========== EXERCÍCIO 2 ===========
# Crie um programa que pede um login e senha. Se o login informado for 'admin' e a senha for 'pass' mostre na tela "Acesso Concedido: {True/False}"

# =========== SOLUÇÃO ===========
login = input("Digite o seu nome de usuário:")
senha = input("Digite sua senha:")

acessoPermitido = login == "admin" and senha == "pass"

print(f"Acesso concedido: {acessoPermitido}")


# =========== EXERCÍCIO 3 ===========
# Crie um programa que pede um número inteiro e verifique se ele é par. Imprima na tela o resultado da verificação:

#Ex: "Par: {True/False}"

# =========== SOLUÇÃO ===========
num = int(input("Digite um número:"))

verificacao = num % 2 == 0

print(f"O número {num} é par: {verificacao}")