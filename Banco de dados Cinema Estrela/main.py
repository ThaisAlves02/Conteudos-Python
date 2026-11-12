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
    print("\nVER FILMES PELO ID")
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

    return resultado[0]

def cadastrarNovoFilme():
    # Cores ANSI para o terminal
    VERDE = '\033[92m'
    VERMELHO = '\033[91m'
    CIANO = '\033[96m'
    AMARELO = '\033[93m'
    NEGRITO = '\033[1m'
    RESET = '\033[0m'

    print(f"\n{CIANO}{'=' * 42}{RESET}")
    print(f"{NEGRITO}{CIANO}🎬      CADASTRO DE UM NOVO FILME      🎬{RESET}")
    print(f"{CIANO}{'=' * 42}{RESET}")

    titulo = input(f"{AMARELO}➤{RESET} Digite o título: ")
    duracao = input(f"{AMARELO}➤{RESET} Digite a duração (ex: 120 min): ")
    classifi = input(f"{AMARELO}➤{RESET} Digite a classificação (ex: 14 anos): ")

    print(f"{CIANO}{'-' * 42}{RESET}")

    try:
        banco.manipular('''
            INSERT INTO filmes
            VALUES (default, %s, %s, %s);
        ''', (titulo, duracao, classifi))
        
        print(f"{VERDE}✅ FILME CADASTRADO COM SUCESSO!{RESET}")
        
    except Exception as error:
        print(f"{VERMELHO}❌ ERRO AO CADASTRAR O FILME:{RESET}")
        print(f"{VERMELHO}   Detalhes: {error}{RESET}")

    print(f"{CIANO}{'=' * 42}{RESET}\n")


def atualizarFilme():
    print("\nATUALIZAR UM FILME")

    resultado = verFilmePorID()
    if resultado is None:
        return

    cod_filme, titulo, duracao, classificacao = resultado
    print("Deixe vazio para manter o valor atual.")
    novo_titulo = input(f"Título {titulo}: ").strip()
    nova_duracao = input(f"Duração {duracao}: ").strip()
    nova_classificacao = input(f"Classificação {classificacao}: ").strip()

    if novo_titulo != "":
        titulo = novo_titulo
    if nova_duracao != "":
        duracao = nova_duracao
    if nova_classificacao != "":
        classificacao = nova_classificacao

    try:
        banco.manipular('''
        UPDATE filmes
        SET (default, %s, %s, %s, %s, %s);                
                        ''', (nome, cpf, cargo, salario, cod_setor))
        print("FUNCIONÁRIO CADASTRADO COM SUCESSO!")
    except Exception as error:
        print("ERRO AO CADASTRAR FUNCIONÁRIO")




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
    elif (op == "3"):
        cadastrarNovoFilme()
    elif (op == "4"):
        atualizarFilme()
    elif (op == "0"):
        print("\nSaindo do programa...")
        
        break
    else:
        print("\nESCOLHA UMA OPÇÃO VÁLIDA")
    
    input("\nTECLE ENTER PARA CONTINUAR")
        