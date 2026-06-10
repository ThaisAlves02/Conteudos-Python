valorFinal = 0
notaFiscal = ""
for i in range(5):
    nome = input(f"Digite o nome do produto {i+1}:")
    preco = float(input(f"Digite o preço do produto {i+1}:"))
    qtd = int(input("Digite a quantidade desejada: "))

    valorCompra = preco * qtd
    valorFinal += valorCompra

    notaFiscal += f"{nome} | R$ {preco:.2f} | {qtd} - R$ {valorCompra:.2f}\n"

print(f"Valor Total á pagar: R${valorFinal}")
print("----- NOTA FISCAL -----")
print("NOME")