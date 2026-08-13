import customtkinter as ctk
from tkinter import messagebox

#messagebox.showinfo('sucesso', 'cliente cadastrado') #messengerbox serve para mostrar uma mensagem ao usuário.
    # Os três tipos de messengerbox: muda só o ícone
    # - messagebox.showinfo
    # - messegerbox.warming
    # - messengerbox.error
    
    # Além das messenger de ação:
    # - messagebox.askyesno
    # - messageboxaskcancel

def cadastrar():
    resposta = messagebox.askyesno('confimar','Deseja cadastrar esse cliente?')
    
    if resposta:
        messagebox.showinfo('Sucesso','Cliente Cadastrado!')
    else:
        messagebox.showwarning('Cancelado', 'Cadastro cancelado')
        
# JANELA


app = ctk.CTk()

app.title("Cadastro de Clientes")
app.geometry("500x400")
app._set_appearance_mode('system')

app.grid_columnconfigure(0,weight=1)
app.grid_columnconfigure(1,weight=1)

# TÍTULO

titulo = ctk.CTkLabel(
    app,
    text="Cadastro de Clientes",
    font=("Arial", 28, "bold")
)

titulo.grid(
    row=0,
    column=0,
    columnspan=2,
    pady=20
)

#FRAME DADOS PESSOAIS

dados_frame = ctk.CTkFrame(app,fg_color="#323b43")

dados_frame.grid(row=1,column=0,columnspan=2,sticky='ew',padx=20)

# NOME


nome_label = ctk.CTkLabel(
    dados_frame,
    text="Nome:"
)

nome_label.grid(
    row=1,
    column=0,
    padx=20,
    pady=10,
    sticky="w"
)

nome_entry = ctk.CTkEntry(
    dados_frame,
    placeholder_text="Digite seu nome",
    width=300,#largura
    height=20,#altura
    corner_radius= 5,#Arredondamento da forma
    border_color="#063a5f", #cor da borda
    border_width=4,#espessura
    text_color="red",#cor do texto do entry
    placeholder_text_color="#c09c49",
    show="*",#caractere que será exibido ao digitar    
)

nome_entry.grid(
    row=1,
    column=1,
    padx=20,
    pady=10
)



# TELEFONE


telefone_label = ctk.CTkLabel(
    dados_frame,
    text="Telefone:"
)

telefone_label.grid(
    row=2,
    column=0,
    padx=20,
    pady=10,
    sticky="w"
)

telefone_entry = ctk.CTkEntry(
   dados_frame,
    placeholder_text="Digite seu telefone",
    width=300
)

telefone_entry.grid(
    row=2,
    column=1,
    padx=20,
    pady=10
)



# E-MAIL


email_label = ctk.CTkLabel(
    dados_frame,
    text="E-mail:"
)

email_label.grid(
    row=3,
    column=0,
    padx=20,
    pady=10,
    sticky="w"
)

email_entry = ctk.CTkEntry(
    dados_frame,
    placeholder_text="Digite seu e-mail",
    width=300
)

email_entry.grid(
    row=3,
    column=1,
    padx=20,
    pady=10
)



# BOTÃO


cadastrar_button = ctk.CTkButton(
    app,
    text="Cadastrar",
    fg_color='red',
    hover_color='blue',
    text_color='grey',
    command=cadastrar
)

cadastrar_button.grid(
    row=4,
    column=0,
    columnspan=2,
    pady=20
)


app.mainloop()