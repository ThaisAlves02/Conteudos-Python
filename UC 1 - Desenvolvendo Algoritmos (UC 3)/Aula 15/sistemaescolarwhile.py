qtdNotasValidas = 0

somaNotasValidas = 0

while True:
    nota = float(input("Digite uma nota entre 0 e 10: "))

    if nota < 0 or nota > 10:
        print("Nota inválida. Digite novamente.")
        continue

    qtdNotasValidas += 1
    somaNotasValidas += nota

    if qtdNotasValidas >= 4:
        break

media = somaNotasValidas/qtdNotasValidas

print(f"Sua média é: {media}")
if media >= 7 and media <= 10:
    print(f"Aprovado.")
elif media >= 4 and media < 7:
    print(f"Recuperação.")
elif media >= 0 and media <= 4:
    print(f"Reprovado.")
else:
    print("Digite uma nota válida!")