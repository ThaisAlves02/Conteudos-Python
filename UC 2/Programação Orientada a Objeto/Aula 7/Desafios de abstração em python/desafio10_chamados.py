from abc import ABC, abstractmethod


class Chamado(ABC):
    @abstractmethod
    def calcular_prazo(self):
        pass


class ChamadoBaixaPrioridade(Chamado):
    def calcular_prazo(self):
        return 72


class ChamadoMediaPrioridade(Chamado):
    def calcular_prazo(self):
        return 48


class ChamadoAltaPrioridade(Chamado):
    def calcular_prazo(self):
        return 24


chamados = [
    ChamadoBaixaPrioridade(),
    ChamadoMediaPrioridade(),
    ChamadoAltaPrioridade()
]

for chamado in chamados:
    prazo = chamado.calcular_prazo()

print(f"""
       ====== PRAZO DE ATENDIMENTO ======
          Baixa Prioridade: {prazo} horas
          Média Prioridade: {prazo} horas
          Alta Prioridade: {prazo} horas
        """)
