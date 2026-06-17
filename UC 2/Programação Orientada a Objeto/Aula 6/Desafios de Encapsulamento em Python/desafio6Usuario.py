class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.__senha = senha

    @property
    def senha(self):
        return "Senha protegida."

    @senha.setter
    def senha(self, nova_senha):
        if len(nova_senha) >= 6:
            self.__senha = nova_senha
            print("Senha alterada com sucesso.")
        else:
            print("A senha deve ter pelo menos 6 caracteres.")

    def mostrar_usuario(self):
        print(f"Usuário: {self.nome}")
        print(self.__senha)


usuario = Usuario("admin", "123456")

usuario.mostrar_usuario()

usuario.senha = "abc"
usuario.mostrar_usuario()

usuario.senha = "abc123"
usuario.mostrar_usuario()
