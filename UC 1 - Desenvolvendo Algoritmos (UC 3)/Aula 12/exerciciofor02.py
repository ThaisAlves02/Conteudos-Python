print("Bem vindo(a) a escola x!")
somadasnotas = 0
contadorNotas = 0

boletim = ""

qtdNotas = int(input("Digite quantas notas serão registradas: "))
for i in range(qtdNotas):
    nota = float(input(f"Digite a nota {i+1}: "))
    if nota >= 0 and nota <= 10:
        somadasnotas += nota
        contadorNotas += 1
        boletim += f"Nota {contadorNotas}: {nota}\n"
    else:
        print("Nota inválida")

media = somadasnotas/contadorNotas
print(f"A média do aluno foi: {media}")

if media >= 6 and media <= 10:
    print("Aprovado!")
elif media >= 4 and media < 6:
    print(f"Recuperação!")
elif media >= 0 and media < 4:
    print(f"Reprovado!")
else:
    print("Média inválida!")

print(f"Boletim: ")

print(boletim)