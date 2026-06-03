"""
== Igualdade
!= Diferença
> Maior que
< Menor que
>= Maior ou Igual
<= Menor ou Igual

is É idêntico a 
in Está dentro de
not Inversão de Valor

Conectores:

and -> "E" Precisa que ambas as afirmações sejam verdadeiras

or -> "OU" Precisa que PELO MENOS UMA afirmação seja verdadeira

"""

# =========== EXERCÍCIO 1 ===========
# Crie um programa que recebe a idade de uma pessoa e exiba na tela se ela pode entar ou não (True ou False). O critério para entrar no sistema é ter idade maior ou igual a 18 anos.

# =========== SOLUÇÃO ===========
idade = int(input("Digite a sua idade:"))

maior_idade = 18
acesso_permitido = idade >= 18

print(f"Acesso ao sistema:{acesso_permitido}")


# =========== EXERCÍCIO 2 ===========
# Crie um programa que pede o nome de um produto, o preço do produto e a quantidade do produto. Calcule o valor total a pagar e exiba na tela. Exiba também True ou False para a meta de venda. Meta é True se a venda for maior ou igual a 100 reais.

# =========== SOLUÇÃO ===========
nome_prod = input("Digite o nome do produto:")
preco_prod = float(input("Digite o preço do produto:"))
quantidade = int(input("Digite a quantidade do produto:"))

valorTotal = preco_prod * quantidade

meta_vendas = valorTotal >= 100

print(f"Valor total á pagar: {valorTotal}\nMeta de venda:{meta_vendas}")




