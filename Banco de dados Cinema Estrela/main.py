from classBanco import Banco

banco = Banco()

def verFilmes():
    print("\n" + "╔" + "═" * 71 + "╗")
    print("║" + "CATÁLOGO DE FILMES".center(71) + "║")
    print("╠" + "═" * 71 + "╣")
    
    filmes = banco.consultar('''
    SELECT f.cod_filme, f.titulo_filme, f.duracao_filme, f.classificacao_filme FROM filmes f
    ORDER BY f.cod_filme ASC;''')
    
    if (len(filmes) == 0):
        print("║" + "NÃO HÁ FILMES CADASTRADOS NO MOMENTO".center(71) + "║")
        print("╚" + "═" * 71 + "╝")
        

    print(f"║ {'CÓDIGO':^6} │ {'TÍTULO DO FILME':<30} │ {'DURAÇÃO':^10} │ {'CLASSIF.':^14} ║")
    print("╟" + "─" * 8 + "┼" + "─" * 32 + "┼" + "─" * 12 + "┼" + "─" * 16 + "╢")

    for cod_fil, titulo_fil, duracao_fil, classificacao_fil in filmes:
        cod_str = str(cod_fil)
        duracao_str = str(duracao_fil)
        classif_str = str(classificacao_fil)
        
        # Se o título for muito grande (mais de 30 letras), corta com "..." para não quebrar a tabela
        titulo_str = str(titulo_fil)
        if len(titulo_str) > 30:
            titulo_str = titulo_str[:27] + "..."

        print(f"║ {cod_str:^6} │ {titulo_str:<30} │ {duracao_str:^10} │ {classif_str:^14} ║")

    print("╚" + "═" * 71 + "╝")


def verFilmePorID():
    print("VER FILMES PELO ID")
    verFilmes()

    filmeescolhido = input("DIGITE O ID DO FILME DESEJADO:")
    
    resultado = banco.consultar('''
    SELECT f.cod_filme, f.titulo_filme, f.duracao_filme, f.classificacao_filme,
           s.cod_sessao, s.data_sessao, s.horario_sessao, s.sala_sessao
    FROM filmes f
    LEFT JOIN sessoes s ON f.cod_filme = s.cod_filme
    WHERE f.cod_filme = %s;''', (filmeescolhido,))

    if len(resultado) == 0:
        print("\n[ERRO] FILME NÃO ENCONTRADO COM ESSE ID!")

    print("\n" + "=" * 50)
    print(f"🎬 FICHA DO FILME #{resultado[0][0]}")
    print("=" * 50)
    print(f"Título:        {resultado[0][1]}")
    print(f"Duração:       {resultado[0][2]}")
    print(f"Classificação: {resultado[0][3]}")
    print("=" * 50)

    print("\n🎟️  SESSÕES DISPONÍVEIS")
    print("-" * 50)
    
    for linha in resultado:
        # linha[4] é o cod_sessao. Se for None, não tem sessão cadastrada
        if linha[4] is None:
            print("Nenhuma sessão cadastrada para este filme.")
        else:
            print(f"Sessão #{linha[4]} | Data: {linha[5]} | Horário: {linha[6]} | Sala: {linha[7]}")
            
    print("-" * 50)
    

def exibirMenu():
        print("\n" + "╔" + "═" * 48 + "╗")
        print("║" + "🎬 SISTEMA CINEMA ESTRELA 🍿".center(46) + "║")
        print("╠" + "═" * 48 + "╣")
        print("║  [1] Listar todos os filmes                    ║")
        print("║  [2] Ver detalhes e sessões de um filme        ║")
        print("║  [3] Cadastrar novo filme                      ║")
        print("║  [4] Atualizar dados de um filme               ║")
        print("║  [5] Excluir filme                             ║")
        print("╟" + "─" * 48 + "╢")
        print("║  [0] Sair do sistema                           ║")
        print("╚" + "═" * 48 + "╝")

while (True):
    exibirMenu()
    
    op = input("DIGITE O NÚMERO DA OPÇÃO DESEJADA:")
    
    if (op == "1"):
        verFilmes()
    elif (op == "2"):
        verFilmePorID()
    elif (op == "0"):
        print("\nSaindo do programa...")
        
        break
    else:
        print("\nESCOLHA UMA OPÇÃO VÁLIDA")
    
    input("\nTECLE ENTER PARA CONTINUAR")
        