from abc import ABC, abstractmethod


class Documento(ABC):
    @abstractmethod
    def imprimir(self):
        pass


class Contrato(Documento):
    def imprimir(self):
        print("Imprimindo contrato empresarial.")


class NotaFiscal(Documento):
    def imprimir(self):
        print("Imprimindo a nota fiscal .")


class Recibo(Documento):
    def imprimir(self):
        print("Imprimindo o recibo.")


documentos = [
    Contrato(),
    NotaFiscal(),
    Recibo()
]

for documento in documentos:
    documento.imprimir()
