animal = {

}

animal["Nome"] = input("Digite o nome do animal: ")

animal["Espécie"] = input("Digite a espécie do animal: ")

animal["Peso"] = float(input("Digite o peso do animal: "))

animal["Idade"] = int(input("Digite a idade do animal: "))


print(f"""
    ----- FICHA DO PACIENTE -----
            Nome: {animal["Nome"]}
            Espécie: {animal["Espécie"]}
            Peso: {animal["Peso"]}
            Idade: {animal["Idade"]}
""")