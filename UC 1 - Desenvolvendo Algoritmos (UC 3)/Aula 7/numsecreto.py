import random
numSecreto = random.randint(0, 10)
palpite = int(input("Digite um número de 0 a 10:"))
if palpite == numSecreto:
    print(f"Você acertou! O número secreto era {numSecreto}")
else:
    print("Você errou!")

    if palpite < numSecreto:
        print(f"O número secreto é maior que o seu palpite. Seu palpite foi {palpite}")
    else:
        print(f"O número secreto é menor que o seu palpite. Seu palpite foi {palpite}")

palpite = int(input("Digite seu novo palpite:"))
if palpite == numSecreto:
    print(f"Você acertou! O número secreto era {numSecreto}")
else:
    pass