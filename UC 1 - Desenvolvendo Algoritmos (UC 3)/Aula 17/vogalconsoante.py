#Crie um programa que recebe uma palavra. Informe se a palavra começa com vogal ou consoante.

make = "batom"

if make[0].lower() in "aeiou":
    print("Começa com vogal")
else:
    print("Começa com consoante")