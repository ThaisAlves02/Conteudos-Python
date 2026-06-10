def calcular_gorjeta1(valor_conta):
    gorjeta = valor_conta * 0.1
    valor_total = gorjeta + valor_conta

    print(f"""
    ======= NOTA FISCAL =======
        Valor da conta: R$ {valor_conta}
        Gorjeta (10%): R$ {gorjeta}
        Total á pagar: R$ {valor_total}
    """)

#calcular_gorjeta1(200)


def calcular_gorjeta2(valor_conta, gorjeta):
    gorjeta = valor_conta * 0.1
    valor_total = valor_conta + gorjeta

    return valor_total

#print(calcular_gorjeta2(600, 0.1))


def calculadora_padrao(num1, num2, op):
    if op == "+":
        resultado = num1 + num2
    elif op == "-":
        resultado = num1 - num2
    elif op == "*":
        resultado = num1 * num2
    elif op == "/":
        if num2 == 0:
            resultado = "Resultado inválido"
        else:
            resultado = num1 / num2

    return resultado


print(calculadora_padrao(20, 30, "+"))


    
