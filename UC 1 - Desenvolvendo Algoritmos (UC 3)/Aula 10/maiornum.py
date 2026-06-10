n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite um número inteiro: "))
n3 = int(input("Digite um número inteiro: "))
if n1 >= n2 and n3:
    print(f"O número {n1} é o maior de todos")
elif n2 >= n3 and n1:
    print(f"O número {n2} é o maior de todos ")
elif n3 >= n2 and n1:
    print(f"O número {n3} é o maior de todos")
else:
    print("Digite um valor válido!")