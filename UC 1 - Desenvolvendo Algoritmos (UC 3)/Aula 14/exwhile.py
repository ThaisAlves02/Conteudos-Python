numero = -1
soma = 0

maior = float("-inf")
menor = float("inf")

contadorNegativos = 0

while numero != 0:
    numero = int(input("Digite um número inteiro (0 para sair): "))
    soma += numero
    
    if numero < 0:
        contadorNegativos += 1

    if maior == None:
        maior = numero

    if numero > maior:
        maior = numero

    if menor == None:
        menor = numero
    
    if numero < menor:
        menor = numero

print(f"Soma: {soma}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
print(f"Quantidade de números negativos: {contadorNegativos}")
