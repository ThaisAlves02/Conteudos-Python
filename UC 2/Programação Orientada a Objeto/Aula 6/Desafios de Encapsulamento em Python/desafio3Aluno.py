class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.__nota = nota
    
    @property
    def nota(self):
        return self.__nota
    
    @nota.setter
    def nota(self, nova_nota):
        if nova_nota > 0 and nova_nota <= 10:
            self.__nota = nova_nota
        else:
            print("NOTA INVÁLIDA!")
            
    def mostrar_nota(self):
        print(f"Aluno: {self.nome}")
        print(f"Nota: {self.nota}")

aluno = Aluno("Bruno", 9)

aluno.mostrar_nota()