import customtkinter as ctk

usuario_correto = "admin"
senha_correta = "123"

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
entrada_senha = ctk.CTkEntry(app,placeholder_text='Senha') #entry é um input
entrada_senha.pack(pady=(10,0))

#Label para mostrar erro de senha
senha_erro = ctk.CTkLabel(app,text="", text_color='red')
senha_erro.pack()

def abrir_tela_principal():
    app.destroy() # Fecha a janela de login
    
    nova_janela = ctk.CTk()
    nova_janela.title('Área principal')
    nova_janela.geometry('400x350')
    nova_janela.mainloop()

def fazer_login():
    usuario = entrada_usuario.get() #get() é para pegar as informações e as guarda
    senha = entrada_senha.get()
    
    if usuario == usuario_correto and senha == senha_correta:
        abrir_tela_principal()
    else:
        senha_erro.configure(text="Usuário ou senha incorretos!")


#Botão do login
botao_login = ctk.CTkButton(app,text='Entrar', command=fazer_login)
botao_login.pack(pady=(10,0))

#Texto para cadastro
texto_cadastro = ctk.CTkLabel(app,text='Cadastre-se', cursor='hand2') #cursor é meu moose 
texto_cadastro.pack()


app.mainloop() #A janela ficará aberta até ser fechada