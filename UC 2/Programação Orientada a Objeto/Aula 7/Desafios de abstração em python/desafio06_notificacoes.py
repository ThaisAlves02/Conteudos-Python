from abc import ABC, abstractmethod


class Notificacao(ABC):
    @abstractmethod
    def enviar(self, mensagem):
        pass


class NotificacaoEmail(Notificacao):
    def enviar(self, mensagem):
        print(f"E-mail enviado: {mensagem}")


class NotificacaoSMS(Notificacao):
    def enviar(self, mensagem):
        print(f"SMS enviado: {mensagem}")


class NotificacaoWhatsApp(Notificacao):
    def enviar(self, mensagem):
        print(f"WhatsApp enviado: {mensagem}")


notificacoes = [
    NotificacaoEmail(),
    NotificacaoSMS(),
    NotificacaoWhatsApp()
]

for notificacao in notificacoes:
    notificacao.enviar("Pedido aprovado com sucesso!")
