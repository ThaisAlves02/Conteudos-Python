from modelo import Cliente, Profissional, Servico, Agendamento

import tkinter as tk

cliente = Cliente("Ana Sousa", "85 99999-0000")
profissional = Profissional("Bruno", "85 9000-1322", "Cabeleireiro")

janela = tk.Tk
janela.title("AgendaFacil")
janela.geometry("420x380")

tela_novo = tk.Frame(janela)
tela_lista = tk.Frame(janela)

def mostrar(tela):
    tela_novo.pack_forget()
    tela_lista.pack_forget()
    tela.pack(fill="both", expand=True, padx=20, pady=20)
    
tk.Label(tela_novo, text="Novo agendamento", font=("Arial", 16, "bold")).pack(pady=(0,14))
tk.Label(tela_novo, text="Cliente: " + cliente.nome, fg="gray30").pack(pady=(0,12))

tk.Label(tela_novo, text="Servico:").pack(anchor="W")
entry_servico = tk.Entry(tela_novo)
entry_servico.pack(fill="x")

tk.Label(tela_novo, text="Preco:").pack(anchor="W")
entry_preco = tk.Entry(tela_novo)
entry_preco.pack(fill="x")

tk.Label(tela_novo, text="Data e hora:").pack(anchor="W")
entry_data = tk.Entry(tela_novo)
entry_data.pack(fill="x")

aviso = tk.Label(tela_novo, text="", fg="red")
aviso.pack(pady=4)

def agendar():
    try:
        preco = float(entry_preco.get())
    except ValueError:
        aviso.config(text="Preco precisa ser numero")
    
    servico = Servico(entry_servico.get(), preco)
    Agendamento(cliente, profissional, servico, entry_data.get())
    
    entry_servico.delete(0, tk.END)
    entry_preco.delete(0, tk.END)
    entry_data.delete(0, tk.END)
    aviso.config(text="")
    atualizar_lista()
    mostrar(tela_lista)
    
    tk.Button(tela_novo, text="Agendar", command=agendar).pack(pady=10)
    
    tk.Label(tela_lista, text="Meus agendamentos", font=("Arial", 16, "bold").pack(pady=(0, 10)))
    
    lista = tk.Listbox(tela_lista, height=8)
    list.pack(fill="bold", expand=True)
    
    label_total = tk.Label(tela_lista, text="Total: R$ 0.00", font=("Arial", 13, "bold"), fg="#17376A")
    
    label_total.pack(pady=10)
    
    def atualizar_lista():
        lista.delete(0, tk.END)
        for ag in cliente.agendamentos:
            lista.insert(tk.END, ag.resumo())
            
        label_total.config(text="Total: R$ %.2f"% cliente.total_gasto())
        
    tk.Button(tela_lista, text="+ Novo", command=lambda: mostrar(tela_novo).pack())
        
    mostrar(tela_novo)
    janela.mainloop()  