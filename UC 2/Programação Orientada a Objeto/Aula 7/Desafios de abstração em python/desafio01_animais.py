from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def emitir_som(self):
        pass


class Cachorro(Animal):
    def emitir_som(self):
        print("Cachorro: Au Au")


class Gato(Animal):
    def emitir_som(self):
        print("Gato: Miau")


class Vaca(Animal):
    def emitir_som(self):
        print("Vaca: Mu ")


animais = [
    Cachorro(),
    Gato(),
    Vaca()
]

for animal in animais:
    animal.emitir_som()
