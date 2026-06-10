soma = 0
contadorpar = 0
for i in range(10):
    numeros = int(input("Digite um número inteiro: "))
    soma += numeros

    if numeros % 2 == 0:
        contadorpar += 1


print(f"A soma dos números é : {soma}")
print(f"A quantidade de números pares é : {contadorpar}")
