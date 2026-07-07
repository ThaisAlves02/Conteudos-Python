from classAluno import Aluno
from classLivro import Livro
from classCarro import Carro

# aluno1 = Aluno("João", "29058")
# aluno1.exibir_informacoes()
# aluno1.situacao_aluno([8,5,10])

# livro1 = Livro("Dom casmurro", "Machado de Assis")

# livro1.reputacao_livro(3)
# livro1.reputacao_livro(1)
# livro1.reputacao_livro(5)
# livro1.reputacao_livro(5)
# livro1.reputacao_livro(3)
# livro1.reputacao_livro(4)

carro = Carro("Volkswagen", "Fusca")
carro2 = Carro("Volkswagen", "Kombi")


carro.descrever()
carro2.descrever()

print(carro.abrir_porta()) 
print(carro.abrir_porta()) 
print(carro.fechar_porta()) 

