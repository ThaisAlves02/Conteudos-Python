from classBanco import Banco
import os 

banco = Banco()

# Paleta de cores minimalista
VERDE = '\033[92m'
VERMELHO = '\033[91m'
CIANO = '\033[96m'
AMARELO = '\033[93m'
NEGRITO = '\033[1m'
RESET = '\033[0m'

def verFilmes():
    print(f"\n{CIANO}┌" + "─" * 71 + f"┐{RESET}")
    print(f"{CIANO}│{NEGRITO}" + "CATÁLOGO DE FILMES".center(71) + f"{RESET}{CIANO}│{RESET}")
    print(f"{CIANO}├" + "─" * 71 + f"┤{RESET}")
    
    filmes = banco.consultar('''
    SELECT f.cod_filme, f.titulo_filme, f.duracao_filme, f.classificacao_filme FROM filmes f
    ORDER BY f.cod_filme ASC;''')
    
    if len(filmes) == 0:
        print(f"{CIANO}│{AMARELO}" + "NÃO HÁ FILMES CADASTRADOS NO MOMENTO".center(71) + f"{RESET}{CIANO}│{RESET}")
        print(f"{CIANO}└" + "─" * 71 + f"┘{RESET}")
        return

    print(f"{CIANO}│{NEGRITO} {'CÓDIGO':^6} │ {'TÍTULO DO FILME':<30} │ {'DURAÇÃO':^10} │ {'CLASSIF.':^14} {RESET}{CIANO}│{RESET}")
    print(f"{CIANO}├" + "─" * 8 + "┼" + "─" * 32 + "┼" + "─" * 12 + "┼" + "─" * 16 + f"┤{RESET}")

    for cod_fil, titulo_fil, duracao_fil, classificacao_fil in filmes:
        cod_str = str(cod_fil)
        duracao_str = str(duracao_fil)
        classif_str = str(classificacao_fil)
        
        titulo_str = str(titulo_fil)
        if len(titulo_str) > 30:
            titulo_str = titulo_str[:27] + "..."

        print(f"{CIANO}│{RESET} {cod_str:^6} {CIANO}│{RESET} {titulo_str:<30} {CIANO}│{RESET} {duracao_str:^10} {CIANO}│{RESET} {classif_str:^14} {CIANO}│{RESET}")

    print(f"{CIANO}└" + "─" * 71 + f"┘{RESET}")


def verFilmePorID():
    verFilmes()

    filmeescolhido = input(f"\n{AMARELO}>{RESET} Digite o ID do filme desejado: ").strip()
    
    resultado = banco.consultar('''
    SELECT f.cod_filme, f.titulo_filme, f.duracao_filme, f.classificacao_filme,
           s.cod_sessao, s.data_sessao, s.horario_sessao, s.sala_sessao
    FROM filmes f
    LEFT JOIN sessoes s ON f.cod_filme = s.cod_filme
    WHERE f.cod_filme = %s;''', (filmeescolhido,))

    if len(resultado) == 0:
        print(f"\n{VERMELHO}[ERRO] Filme não encontrado com esse ID.{RESET}")
        return None

    print(f"\n{CIANO}┌" + "─" * 58 + f"┐{RESET}")
    print(f"{CIANO}│{NEGRITO}" + f"FICHA DO FILME #{resultado[0][0]}".center(58) + f"{RESET}{CIANO}│{RESET}")
    print(f"{CIANO}├" + "─" * 58 + f"┤{RESET}")
    print(f"{CIANO}│{RESET} {NEGRITO}Título:{RESET}        {str(resultado[0][1]):<41} {CIANO}│{RESET}")
    print(f"{CIANO}│{RESET} {NEGRITO}Duração:{RESET}       {str(resultado[0][2]):<41} {CIANO}│{RESET}")
    print(f"{CIANO}│{RESET} {NEGRITO}Classificação:{RESET} {str(resultado[0][3]):<41} {CIANO}│{RESET}")
    print(f"{CIANO}├" + "─" * 58 + f"┤{RESET}")
    print(f"{CIANO}│{NEGRITO}" + "SESSÕES DISPONÍVEIS".center(58) + f"{RESET}{CIANO}│{RESET}")
    print(f"{CIANO}├" + "─" * 58 + f"┤{RESET}")
    
    for linha in resultado:
        if linha[4] is None:
            print(f"{CIANO}│{AMARELO}" + "Nenhuma sessão cadastrada para este filme.".center(58) + f"{RESET}{CIANO}│{RESET}")
        else:
            texto_sessao = f"Sessão #{linha[4]} | Data: {linha[5]} | Hora: {linha[6]} | Sala: {linha[7]}"
            print(f"{CIANO}│{RESET} {texto_sessao:<56} {CIANO}│{RESET}")
            
    print(f"{CIANO}└" + "─" * 58 + f"┘{RESET}")

    return resultado[0]


def cadastrarNovoFilme():
    print(f"\n{CIANO}{NEGRITO}=== CADASTRAR NOVO FILME ==={RESET}")

    titulo = input(f"{AMARELO}>{RESET} Título: ").strip()
    duracao = input(f"{AMARELO}>{RESET} Duração (ex: 02:00:00): ").strip()
    classifi = input(f"{AMARELO}>{RESET} Classificação (ex: 14 anos): ").strip()

    try:
        banco.manipular('''
            INSERT INTO filmes
            VALUES (default, %s, %s, %s);
        ''', (titulo, duracao, classifi))
        
        print(f"\n{VERDE}[OK] Filme cadastrado com sucesso!{RESET}")
        
    except Exception as error:
        print(f"\n{VERMELHO}[ERRO] Falha ao cadastrar filme: {error}{RESET}")


def atualizarFilme():
    print(f"\n{CIANO}{NEGRITO}=== ATUALIZAR DADOS DO FILME ==={RESET}")

    resultado = verFilmePorID()
    if resultado is None:
        return

    continuar = input(f"\n{AMARELO}>{RESET} Deseja alterar as informações deste filme? (S/N): ").strip().upper()

    if continuar != "S":
        print(f"{AMARELO}[AVISO] Operação cancelada.{RESET}")
        return

    cod, titulo, duracao, classificacao = resultado[:4]

    print(f"\n{CIANO}Deixe em branco e tecle Enter para manter o valor atual:{RESET}")

    novo_titulo = input(f"{AMARELO}>{RESET} Novo título ({titulo}): ").strip()
    if novo_titulo:
        titulo = novo_titulo

    nova_duracao = input(f"{AMARELO}>{RESET} Nova duração ({duracao}): ").strip()
    if nova_duracao:
        duracao = nova_duracao

    nova_classificacao = input(f"{AMARELO}>{RESET} Nova classificação ({classificacao}): ").strip()
    if nova_classificacao:
        classificacao = nova_classificacao

    try:
        banco.manipular('''
            UPDATE filmes
            SET titulo_filme = %s,
                duracao_filme = %s,
                classificacao_filme = %s
            WHERE cod_filme = %s;
        ''', (titulo, duracao, classificacao, cod))
        print(f"\n{VERDE}[OK] Filme atualizado com sucesso!{RESET}")
    except Exception as error:
        print(f"\n{VERMELHO}[ERRO] Falha na atualização: {error}{RESET}")


def excluirFilme():
    print(f"\n{CIANO}{NEGRITO}=== EXCLUIR FILME ==={RESET}")

    resultado = verFilmePorID()
    if not resultado:
        return

    continuar = input(f"\n{VERMELHO}>{RESET} Deseja realmente apagar esse filme? (S/N): ").strip().upper()

    if continuar != "S":
        print(f"{AMARELO}[AVISO] Operação cancelada.{RESET}")
        return

    try:
        banco.manipular('''
            DELETE FROM filmes
            WHERE cod_filme = %s;
        ''', (resultado[0],))
        print(f"\n{VERDE}[OK] Filme removido com sucesso!{RESET}")
    except Exception:
        print(f"\n{VERMELHO}[ERRO] Não foi possível remover o filme. Verifique se há sessões vinculadas.{RESET}")



def limparTela():
    # Executa 'cls' no terminal se for Windows ('nt'), ou 'clear' se for Linux/Mac
    os.system('cls')

def exibirMenu():
    print(f"\n{CIANO}┌" + "─" * 46 + f"┐{RESET}")
    print(f"{CIANO}│{NEGRITO}" + "SISTEMA CINEMA ESTRELA".center(46) + f"{RESET}{CIANO}│{RESET}")
    print(f"{CIANO}├" + "─" * 46 + f"┤{RESET}")
    print(f"{CIANO}│{RESET} {AMARELO}[1]{RESET} Listar todos os filmes                   {CIANO}│{RESET}")
    print(f"{CIANO}│{RESET} {AMARELO}[2]{RESET} Ver detalhes e sessões de um filme       {CIANO}│{RESET}")
    print(f"{CIANO}│{RESET} {AMARELO}[3]{RESET} Cadastrar novo filme                     {CIANO}│{RESET}")
    print(f"{CIANO}│{RESET} {AMARELO}[4]{RESET} Atualizar dados de um filme              {CIANO}│{RESET}")
    print(f"{CIANO}│{RESET} {AMARELO}[5]{RESET} Excluir filme                            {CIANO}│{RESET}")
    print(f"{CIANO}├" + "─" * 46 + f"┤{RESET}")
    print(f"{CIANO}│{RESET} {VERMELHO}[0]{RESET} Sair do sistema                          {CIANO}│{RESET}")
    print(f"{CIANO}└" + "─" * 46 + f"┘{RESET}")


while True:
    limparTela()
    exibirMenu()
    
    op = input(f"\n{AMARELO}>{RESET} Escolha uma opção: ").strip()
    limparTela()
    
    if op == "1":
        verFilmes()
    elif op == "2":
        verFilmePorID()
    elif op == "3":
        cadastrarNovoFilme()
    elif op == "4":
        atualizarFilme()
    elif op == "5":
        excluirFilme()
    elif op == "0":
        limparTela()
        print(f"\n{CIANO}Encerrando o sistema... Até logo!{RESET}")
        break
    else:
        print(f"\n{VERMELHO}[ERRO] Opção inválida.{RESET}")
    
    input(f"\n{CIANO}Pressione Enter para continuar...{RESET}")