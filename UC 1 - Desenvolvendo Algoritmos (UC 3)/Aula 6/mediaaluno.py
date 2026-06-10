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