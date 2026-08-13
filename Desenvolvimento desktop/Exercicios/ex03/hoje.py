import customtkinter as ctk
from tkinter import messagebox


# =====================================================
# EXERCÍCIO: FRAMES, CORES E BOTÕES
# =====================================================
# Objetivo: praticar CTkFrame, fg_color, hover_color,
# sticky, columnconfigure e corner_radius.
#
# Partes marcadas com # TODO são para você completar.
# O resto já está pronto como exemplo/referência.
# =====================================================


app = ctk.CTk()
app.title("Painel de Controle")
app.geometry("700x500")

# A coluna 0 vai crescer e ocupar o espaço extra da janela
app.columnconfigure(0, weight=1)


# =====================================================
# CABEÇALHO (frame já pronto, de exemplo)
# =====================================================

header_frame = ctk.CTkFrame(
    app,
    fg_color="#1f6aa5",
    corner_radius=15
)

header_frame.grid(
    row=0,
    column=0,
    padx=20,
    pady=(20, 10),
    sticky="ew"     # estica na horizontal
)

# Dentro do header, o título fica centralizado (sem sticky)
titulo_label = ctk.CTkLabel(
    header_frame,
    text="Painel de Controle",
    font=("Arial", 26, "bold"),
    text_color="white"
)

titulo_label.grid(
    row=0,
    column=0,
    padx=20,
    pady=15
)


# =====================================================
# SEÇÃO DE STATUS (frame já pronto, de exemplo)
# =====================================================

status_frame = ctk.CTkFrame(
    app,
    fg_color="#2b2b2b",
    corner_radius=15
)

status_frame.grid(
    row=1,
    column=0,
    padx=20,
    pady=10,
    sticky="ew"
)

status_frame.columnconfigure(0, weight=1)  # o texto de status vai esticar

status_label = ctk.CTkLabel(
    status_frame,
    text="Status: aguardando ação...",
    font=("Arial", 14),
    anchor="w"          # alinha o texto à esquerda dentro do espaço esticado
)

status_label.grid(
    row=0,
    column=0,
    padx=20,
    pady=15,
    sticky="ew"
)


def atualizar_status(mensagem):
    """Função pronta: atualiza o texto do status_label."""
    status_label.configure(text=f"Status: {mensagem}")


# =====================================================
# TODO 1: crie um frame verde chamado "sucesso_frame"
# =====================================================
# - fg_color="#2fa572"
# - corner_radius=15
# - grid: row=2, column=0, padx=20, pady=10, sticky="ew"
#
# Dentro dele, crie um CTkButton com:
# - text="Ação Concluída"
# - fg_color="#207a52"
# - hover_color="#1c6944"
# - command deve chamar atualizar_status("ação concluída com sucesso!")
#
# Dica: primeiro cria o frame e dá .grid() nele.
# Depois cria o botão com sucesso_frame como pai (primeiro argumento).


# TODO 1 - escreva seu código aqui:
sucesso_frame = ctk.CTkFrame(app,fg_color="#8ac8ff")
sucesso_frame.grid(row=1,column=2,columnspan=2,sticky='ew',padx=20)


# =====================================================
# TODO 2: crie um frame vermelho chamado "perigo_frame"
# =====================================================
# - fg_color="#b3261e"
# - corner_radius=15
# - grid: row=3, column=0, padx=20, pady=10, sticky="ew"
#
# Dentro dele, crie um CTkButton com:
# - text="Excluir Tudo"
# - fg_color="#8c1c16"
# - hover_color="#6e1611"
# - command deve mostrar um messagebox.askyesno perguntando
#   "Tem certeza que deseja excluir tudo?" e, se a resposta for
#   True, chamar atualizar_status("tudo foi excluído.")


# TODO 2 - escreva seu código aqui:






app.mainloop()