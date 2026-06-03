# 1. Crie um programa que pergunta se uma pessoa tem reserva para o restaurante. Verifique se a resposta foi especificamente "Sim" e imprima o resultado da verificação:

#Ex: "Entrada Permitida: {True/False}"

print("Bem vindo ao Restaurante XYZ")
reserva = input("Você tem reserva?(Sim/Não)")

resposta = reserva == "Sim"

print(f"Entrada permitida: {resposta}")