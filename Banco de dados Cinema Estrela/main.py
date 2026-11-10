from classBanco import Banco

banco = Banco()

def verFilmes():
    print("LISTA DE FILMES")
    
    filmes = banco.consultar('''
    SELECT f.cod_filme, f.titulo_filme, f.duracao_filme, f.classificacao_filme FROM filmes f
    ORDER BY f.cod_filme ASC;''')
    
    if (len(filmes) == 0):
        print("NÃO HÁ FILMES CADASTRADOS")

    print(f"CODIGO | TITULO | DURACAO | CLASSIFICACAO")
    for cod_fil, titulo_fil, duracao_fil, classificacao_fil in filmes:
        print(f'''{cod_fil} | {titulo_fil} | {duracao_fil} | {classificacao_fil}''')

def verFilmePorID():
    print("VER FILMES PELO ID")
    verFilmes()

    filmeescolhido = input("DIGITE O ID DO FILME DESEJADO:")
    
    resultado = banco.consultar('''
    SELECT f.cod_filme, f.titulo_filme, f.duracao_filme, f.classificacao_filme 
    FROM filmes f
    WHERE f.cod_filme = %s;''', (filmeescolhido,))

    if len(resultado) == 0:
        print("\n[ERRO] FILME NÃO ENCONTRADO COM ESSE ID!")

    print("DETALHES DO FILME")
    for cod_fil, titulo_fil, duracao_fil, classificacao_fil in resultado:
        print(f'''{cod_fil} | {titulo_fil} | {duracao_fil} | {classificacao_fil}''')


while (True):
    print('''
          BEM VINDO AO CINEMA ESTRELA
          
          MENU:
          
          1. Ver filmes
          2. Ver filme por id
          
          0. Sair
          ''')
    
    op = input("DIGITE O NÚMERO DA OPÇÃO DESEJADA:")
    
    if (op == "1"):
        verFilmes()
    elif (op == "2"):
        verFilmePorID()
    elif (op == "0"):
        print("Saindo do programa...")
        
        break
    else:
        print("ESCOLHA UMA OPÇÃO VÁLIDA")
    
    input("TECLE ENTER PARA CONTINUAR")
        