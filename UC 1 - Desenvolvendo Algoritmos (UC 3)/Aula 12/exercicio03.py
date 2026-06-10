import random
numSecreto = random.randint(0,10)
tentativas = 3
for i in range(tentativas):
    print("Você tem 3 tentativas")
    palpite = int(input("Dê um palpite de 0 á 10: "))
    tentativas -= 1
    if palpite == numSecreto:
        print(f"Você acertou! O número secreto é: {numSecreto}.")
        break
    else:
        if tentativas == 0:
            print("Você gastou todas as suas tentativas! Tente novamente.")
        else:
            print("Você errou!")

print("Fim de jogo!")