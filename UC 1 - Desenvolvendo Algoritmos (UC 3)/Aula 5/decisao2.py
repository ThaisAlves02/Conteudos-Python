# 2.Receba o nome de um animal se o animal for gato imprima "Miau Miau", se o animal for cachorro imprima "Au Au", se o animal for papagaio imprima "Lôro quer biscoito" se não for nenhum dos animais imprima "Animal Não Catalogado".

nomeAnimal = input("Digite o nome do animal:")

if nomeAnimal == "Gato":
    print("Miau Miau")
elif nomeAnimal == "Cachorro":
    print("Au Au")
elif nomeAnimal == "Papagaio":
    print("Lôro quer biscoito")
else:
    print("Animal não catalogado")