import customtkinter as ctk
from tkinter import messagebox

def cadastrar():
    resposta = messagebox.askyesno('Confirmar, Deseja cadastrar esse cliente?')
    if resposta:
        messagebox.showinfo('cliente cadastrado!')
    else:
        messagebox.showwarning('Cancelado')
    #messagebox.showinfo('sucesso', 'cliente cadastrado') #messengerbox serve para mostrar uma mensagem ao usuário.
    # Os três tipos de messengerbox: muda só o ícone
    # - messagebox.showinfo
    # - messegerbox.warming
    # - messengerbox.error
    
    # Além das messenger de ação:
    # - messagebox.askyesno
    # - messageboxaskcancel

app = ctk.CTk()
app.title('Cadastro')
app.geometry('500x400')
app._set_appearance_mode('system')


titulo = ctk.CTkLabel(
    app,
    text='Cadastro de clientes',
    font=('Arial',20,'bold'),
    padx=10,
)

titulo.grid(
    row=0, # row é linha
    column = 0,
    padx=10,
    columnspan =3
)

label_nome = ctk.CTkLabel(
    app,
    text='Nome',
    pady=10
)

label_nome.grid(
    row=1,
    column=0,
    sticky='w', # wens: w = esquerda, e = direita, n = cima, s = baixo
    padx=10
)

entry_nome = ctk.CTkEntry(
    app,
    placeholder_text='Digite seu nome',
    #corner_radius=5, #arredonda as bordas
    #border_color='light blue' #dar cor as bordas
    #border_width=4, # espessura
    #text_color='red',
    #placeholder_text_color='yellow'
    #show='*' # O caractere * será exibido quando eu digitar
)

entry_nome.grid(
    row=1,
    column=1,
    pady=10
)

label_telefone = ctk.CTkLabel(
    app,
    text='Telefone',
)

label_telefone.grid(
    row=2,
    column=0,
    sticky='w', # wens: w = esquerda, e = direita, n = cima, s = baixo
    padx=10
)

entry_telefone = ctk.CTkEntry(
    app,
    placeholder_text='Digite seu telefone'
)

entry_telefone.grid(
    row=2,
    column=1,
    pady=10
)

label_email = ctk.CTkLabel(
    app,
    text='Email',
    pady=10
)

label_email.grid(
    row=3,
    column=0,
    sticky='w', # wens: w = esquerda, e = direita, n = cima, s = baixo
    padx=10
)

entry_email = ctk.CTkEntry(
    app,
    placeholder_text='Digite seu email'
)

entry_email.grid(
    row=3,
    column=1,
    pady=10
)

cadastrar_botao = ctk.CTkButton(
    app,
    text='Cadastrar',
    fg_color='red', #cor do botão
    hover_color='blue', #muda de cor quando passo o mouse em cima do botão
    command=cadastrar
)

cadastrar_botao.grid(
    row=4,
    column=0,
    columnspan=2 #consegue ficar nas duas colunas que ele está
)

app.mainloop()