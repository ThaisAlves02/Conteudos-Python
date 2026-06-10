while True:
    num1 = float(input("Digite o número 1: "))
    num2 = float(input("Digite o número 2: "))
    operacao = input("Qual operação você deseja realizar? (+, -, *, /): ")
    resultado = 0

    if operacao == "+":
        resultado = num1 + num2

    elif operacao == "-":
        resultado = num1 - num2

    elif operacao == "*":
        resultado = num1 * num2

    elif operacao == "/":
        if num2 == 0:
            resultado = "TENTATIVA DE DIVISÃO POR 0!"
        else:
            resultado = num1 / num2
    
    print(f"{num1} {operacao} {num2} = {resultado}")

    resposta = input("Deseja realizar outra operação? (Sim/Não): ")
    
    if resposta == "Não":
        print("Encerrando a calculadora...")
        break
    elif resposta == "Sim":
        continue