maior = None
menor = None
for i in range(5):
    num = float(input("Digite um número real: "))

    if maior == None:
        maior = num
    if num < menor:
        menor = num

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")