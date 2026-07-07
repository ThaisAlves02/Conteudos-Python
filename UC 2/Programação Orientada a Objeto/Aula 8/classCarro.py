class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.porta = False 
    
    def detalhes_carro(self):
        return f"Carro modelo {self.modelo}, fabricante {self.marca}"
    
    def descrever(self):
        print(f"Marca: {self.marca} | Modelo: {self.modelo}")
    
    def abrir_porta(self):
        if self.porta == False:
            self.porta = True 
            return f"Abrindo a porta do {self.modelo}..."
        else:
            return f"A porta do {self.modelo} já está aberta!"
            
    def fechar_porta(self):
        if self.porta == True:
            self.porta = False 
            return f"Fechando a porta do {self.modelo}..."
        else:
            return f"A porta do {self.modelo} já está fechada!"


