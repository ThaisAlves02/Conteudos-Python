class Pessoa:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
    
class Cliente(Pessoa):
    def __init__(self, nome,telefone):
        super().__init__(nome, telefone)
        self.agendamentos = []
    
    def total_gasto(self):
        total = 0
        for ag in self.agendamentos:
            total += ag.servico.get_preco()
        return total
    
    def apresentar(self):
        return f"{self.nome} {cliente}"
    
class Profissional(Pessoa):
    def __init__(self, nome, telefone, especialidade):
        super().__init__(nome, telefone)
        self.especialidade = especialidade
        self.agendamentos = []
        
    def apresentar(self):
        return f"{self.nome} ({self.especialidade})"
    
    def agenda_do_dia(self, data):
        return [ag.resumo() for ag in self.agendamentos
                if ag.data_hora.startswith(data)]
    
class Servico:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def get_preco(self):