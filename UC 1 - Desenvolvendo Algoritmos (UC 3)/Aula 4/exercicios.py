# =========== EXERCÍCIO 1 ===========
# Crie um programa que pede o nome da pessoa e o ano de nascimento da pessoa. Exiba o nome e a idade da pessoa.

# =========== SOLUÇÃO ===========
nome = input("Digite seu nome:")
anoNascimento = int(input("Digite seu ano de nascimento:"))

anoAtual = 2026
idade = anoAtual - anoNascimento

print(f"Olá {nome}, você tem {idade} anos.")


# =========== EXERCÍCIO EXTRA ===========

# =========== SOLUÇÃO ===========
print("Seja bem-vindo ao programa!")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

print(f"Olá, {nome}! Você tem {idade} anos e sua altura é {altura}.")


# =========== EXERCÍCIO 2 ===========
# Crie um programa que recebe o nome de um produto, o preço e a quantidade comprada desse produto. Exiba ao final o valor total a pagar desse produto.

# =========== SOLUÇÃO ===========
nomeProduto = input("Digite o nome do produto:")
preco = float(input("Digite o preço do produto:"))
quantidade = int(input("Digite a quantidade do produto:"))

total = preco * quantidade

print(f"O valor total á pagar é: R$ {total}")


# =========== EXERCÍCIO 3 ===========
# Crie um programa que pede o nome de um aluno e suas 4 notas. Ao final exiba a média do aluno.

# =========== SOLUÇÃO ===========
nome = input("Digite seu nome:")
n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))
n3 = float(input("Digite a terceira nota:"))
n4 = float(input("Digite a quarta nota:"))

media = (n1 + n2 + n3 + n4) / 4

print(f"Olá {nome}, a sua média é:{media:.2f} {"Aprovado!" if media >=7 else "Reprovado"}")

