from abc import ABC, abstractmethod


class Pagamento(ABC):
    @abstractmethod
    def pagar(self, valor):
        pass


class PagamentoPix(Pagamento):
    def pagar(self, valor):
        print(f"Pagamento via Pix no valor de R$ {valor:.2f}")


class PagamentoCartao(Pagamento):
    def pagar(self, valor):
        print(f"Pagamento via cartão no valor de R$ {valor:.2f}")


class PagamentoBoleto(Pagamento):
    def pagar(self, valor):
        print(f"Pagamento via boleto no valor de R$ {valor:.2f}")


pagamentos = [
    PagamentoPix(),
    PagamentoCartao(),
    PagamentoBoleto()
]

for pagamento in pagamentos:
    pagamento.pagar(400)
