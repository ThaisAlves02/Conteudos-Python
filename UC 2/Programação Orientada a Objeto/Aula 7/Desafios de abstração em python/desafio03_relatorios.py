from abc import ABC, abstractmethod


class Relatorio(ABC):
    @abstractmethod
    def gerar(self, dados):
        pass


class RelatorioPDF(Relatorio):
    def gerar(self, dados):
        print(f"Gerando relatório PDF: {dados}")


class RelatorioExcel(Relatorio):
    def gerar(self, dados):
        print(f"Gerando relatório Excel: {dados}")


class RelatorioHTML(Relatorio):
    def gerar(self, dados):
        print(f"Gerando relatório HTML: {dados}")


relatorios = [
    RelatorioPDF(),
    RelatorioExcel(),
    RelatorioHTML()
]

for relatorio in relatorios:
    relatorio.gerar("Produtos em estoque")
