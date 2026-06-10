estoque = ["arroz", "feijão", "macarrão", "leite", "óleo"]

produto = input("Escreva o produto desejado: ")

if produto in estoque:
    print("PRODUTO DISPONÍVEL")
else:
    print("PRODUTO INDISPONÍVEL")

estoque_alfabetico = sorted(estoque)

ordem = 1
for p in estoque:
    print(f"{ordem} - {p}")
    ordem += 1