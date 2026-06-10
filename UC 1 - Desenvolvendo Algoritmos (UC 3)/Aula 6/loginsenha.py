login = input("Digite o seu nome de usuário:")
senha = input("Digite sua senha:")
acessoPermitido = login == "admin" and senha == "pass"
print(f"Acesso concedido: {acessoPermitido}")