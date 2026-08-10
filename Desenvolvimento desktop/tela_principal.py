import customtkinter as ctk

#Criar a janela principal
app = ctk.CTk()
app.title('Login') #tela de login
app.geometry('400x350') #Largura e altura da tela

#Titulo
titulo = ctk.CTkLabel(app,text="Bem-vindo!",font=('Arial',24,'bold'))
titulo.pack(pady=(40,10)) #.pack faz a minha label aparecer

#subtitulo
subtitulo = ctk.CTkLabel(app,text='Faça login para continuar')
subtitulo.pack(pady=(0,20))

#campo de usuário
entrada_usuario = ctk.CTkEntry(app,placeholder_text='Usuário') #entry é um input
entrada_usuario.pack()

#campo de senha
senha = ctk.CTkEntry(app,placeholder_text='Senha') #entry é um input
senha.pack(pady=(10,0))

#Botão do login
botao_login = ctk.CTkButton(app,text='Entrar')
botao_login.pack(pady=(10,0))

app.mainloop() #A janela ficará aberta até ser fechada