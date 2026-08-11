import customtkinter as ctk

tela = ctk.CTk()
tela.title('IMC')
tela.geometry('400x350')

titulo = ctk.CTkLabel(tela,text='Calculadora de IMC',font=('Arial',16,'bold'))
titulo.pack(pady=(40,10))

entrada_peso = ctk.CTkEntry(tela,placeholder_text='Digite o seu peso')
entrada_peso.pack()

entrada_altura = ctk.CTkEntry(tela,placeholder_text='Digite a sua altura')
entrada_altura.pack(pady=(10,0))

def calcular_imc():
    peso = float(entrada_peso.get())
    altura = float(entrada_altura.get())
    
    imc = peso / (altura * altura)
    mensagem.configure(text=f"Seu IMC é: {imc:.2f}") # .configure é parecido com o replace.
    

botao = ctk.CTkButton(tela,text='Calcular', command=calcular_imc)
botao.pack(pady=(10,0))

mensagem = ctk.CTkLabel(tela,text="", text_color='lightblue')
mensagem.pack(pady=3)

tela.mainloop()


#Sugestão de melhoria: Uma melhoria bem legal seria mostrar a classificação do IMC junto com o resultado.
#Assim o programa deixa de apenas calcular o número e passa a informar se está abaixo do peso, normal, sobrepeso etc.
#Também recomendo colocar try/except, porque atualmente se o usuário digitar uma letra ou deixar o campo vazio, o programa quebra.