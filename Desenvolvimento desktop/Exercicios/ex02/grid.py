import customtkinter as ctk

app = ctk.CTk()
app.title('Cadastro')
app.geometry('500x400')

titulo = ctk.CTkLabel(
    app,
    text='Cadastro de clientes',
    font=('Arial',20,'bold'),
    padx=10
)
titulo.grid(
    row=0, # row é linha
    column = 0,
    padx=10,
    columnspan =2
)

label_nome = ctk.CTkLabel(
    app,
    text='Nome',
)

label_nome.grid(
    row=1,
    column=0,
    sticky='w', # wens: w = esquerda, e = direita, n = cima, s = baixo
    padx=10
)

entry_nome = ctk.CTkEntry(
    app,
    placeholder_text='Digite seu nome'
)

entry_nome.grid(
    row=1,
    column=1
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
    row=1,
    column=1
)

app.mainloop()