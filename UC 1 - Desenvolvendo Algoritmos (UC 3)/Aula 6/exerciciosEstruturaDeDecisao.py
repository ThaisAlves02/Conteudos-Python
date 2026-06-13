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


# =========== EXERCÍCIO 3 ===========
# Receba a nota de um aluno, imprima "Aprovado" se a nota for maior ou igual a 7, se não imprima "Reprovado".

# =========== SOLUÇÃO ===========
notaAluno = float(input("Digite a nota do aluno:"))

if notaAluno >= 7:
    print("Aprovado!")
else:
    print("Reprovado!")

# =========== EXERCÍCIO 4 ===========
# Receba o nome de um animal se o animal for gato imprima "Miau Miau", se o animal for cachorro imprima "Au Au", se o animal for papagaio imprima "Lôro quer biscoito" se não for nenhum dos animais imprima "Animal Não Catalogado".

# =========== SOLUÇÃO ===========
nomeAnimal = input("Digite o nome do animal:")

if nomeAnimal == "Gato":
    print("Miau Miau")

elif nomeAnimal == "Cachorro":
    print("Au Au")

elif nomeAnimal == "Papagaio":
    print("Lôro quer biscoito")

else:
    print("Animal não catalogado")

# =========== EXERCÍCIO 5 ===========
# Melhore o programa do aluno para: Escreva um programa que recebe 4 notas, calcule a média do aluno e imprima na tela a média calculada e a situação de acordo com a seguinte regra:

#media maior ou igual a 7 e media menor ou igual a 10: aprovado
#media menor que 7 e media maior ou igual a 4: recuperação
#media menor que 4 e media maior ou igual a 0: reprovado

# =========== SOLUÇÃO ===========
n1 = float(input("Digite nota 1:"))
n2 = float(input("Digite nota 2:"))
n3 = float(input("Digite nota 3:"))
n4 = float(input("Digite nota 4:"))

media = (n1 + n2 + n3 + n4)/4

if media >= 7 and media <= 10:
    print(f"Aprovado! A sua média é:{media} ")

elif media < 7 and media >= 4:
    print(f"Recuperação! A sua média é:{media}")

elif media < 4 and media >= 0:
    print(f"Reprovado! A sua média é:{media}")
    
else:
    print("Escreva uma nota válida!")


