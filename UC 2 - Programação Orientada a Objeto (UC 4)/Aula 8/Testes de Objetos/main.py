from classAluno import Aluno
from classLivro import Livro
from classPokemon import Pokemon

# CLASSE ALUNO
aluno1 = Aluno("Lucas", 18, [10,9,7,8])
aluno2 = Aluno("Sabrina", 19, [10,10,7,8])
aluno3 = Aluno("Bruno", 17, [7,6,7,8])

aluno1.mostrar_informacoes()
aluno2.mostrar_informacoes()
aluno3.mostrar_informacoes()

# -------------------------------------------------------------------------
# CLASSE LIVRO

livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
livro2 = Livro("Alice no país das maravilhas", "Lewis Carroll", 865)
livro3 = Livro(" Percy Jackson e o Ladrão de Raios", "Rick Riordan", 1964)

livro1.mostrar_informacoes()
livro2.mostrar_informacoes()
livro3.mostrar_informacoes()

# -------------------------------------------------------------------------
# CLASSE POKÉMON

pokemon1 = Pokemon("Charizard", 223, 173)
pokemon2 = Pokemon("Pikachu", 112, 96)
pokemon3 = Pokemon("Bulbasaur", 118, 111)

pokemon1.mostrar_informacoes()
pokemon2.mostrar_informacoes()
pokemon3.mostrar_informacoes()


