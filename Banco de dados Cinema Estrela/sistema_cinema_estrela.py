# 1. Criar um aplicativo python para visualizar os dados do cinema

# 2. As opções do menu devem ser:
    # 1 - Ver Filmes
    # 2 - Ver Sessões
    # 3 - Cadastrar novo filme
    # 4 - Cadastrar nova sessão
    
# 3. Funcionalidades extras:
    # - Ver detalhes de um filme (a pessoa escolhe um filme da lista e vê somente informações daquele filme)
    # - Ao ver uma sessão, exibir o nome do filme da sessão

import os
import psycopg
from dotenv import load_dotenv
from datetime import time

load_dotenv()


while True:
    
    
    
    print("""
    SEJA BEM VINDO AO CINEMA ESTRELA
    
    MENU:
    
    1 - Ver Filmes
    2 - Ver Sessões
    3 - Cadastrar novo filme
    4 - Cadastrar nova sessão
    
    0 - Sair      
    
          """)
    
    op = input("Digite a opção desejada: ")

    if (op == "1"):
        print("VER FILMES\n")

        filmes = None

        conexaoDB = None
        cursor = None

        try:
            conexaoDB = psycopg.connect(
                    host=os.getenv("DB_HOST"),
                    port=os.getenv("DB_PORT"),
                    dbname=os.getenv("DB_NAME"),
                    user=os.getenv("DB_USER"),
                    password=os.getenv("DB_PASSWORD"),
                    sslmode=os.getenv("DB_SSL")
                )
            cursor = conexaoDB.cursor()
            
            cursor.execute("SELECT * FROM filmes;")
            
            filmes = cursor.fetchall()

        except Exception as error:
            print("OCORREU UM ERRO:",error)
            if (conexaoDB is not None):
                conexaoDB.rollback()
        finally:
            if (cursor is not None):
                cursor.close()
            
            if (conexaoDB is not None):
                conexaoDB.close()

        print("LISTA DE FILMES")
        print("TÍTULO | DURAÇÃO | CLASSIFICAÇÃO")

        if (filmes):
            for fil in filmes:
                print(f"{fil[0]} | {fil[1]} | {fil[2]} | {fil[3]}")
        else:
            print("ERRO! NÃO FOI POSSÍVEL VER OS FILMES.")

    elif (op == "2"):
        print("VER SESSOES\n")

        sessoes = None

        conexaoDB = None
        cursor = None

        try:
            conexaoDB = psycopg.connect(
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT"),
                dbname=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                sslmode=os.getenv("DB_SSL")
            )
            cursor = conexaoDB.cursor()
            
            cursor.execute("SELECT * FROM sessoes;")
            
            sessoes = cursor.fetchall()

        except Exception as error:
            print("OCORREU UM ERRO:",error)
            if (conexaoDB is not None):
                conexaoDB.rollback()
        finally:
            if (cursor is not None):
                cursor.close()
            
            if (conexaoDB is not None):
                conexaoDB.close()

            print("LISTA DE SESSOES")
            print("DATA | HORÁRIO | SESSOES")

            if (sessoes):
                for se in sessoes:
                    print(f"{se[0]} | {se[1]} | {se[2].strftime("%d/%m/%y")} | {se[3]}")
            else:
                print("ERRO! NÃO FOI POSSÍVEL VER AS SESSOES.")

    elif (op == "3"):
        print("CADASTRAR NOVO FILME")

        titulo = input("Digite o título:")
        duracao = input("Digite a duração (HH:MM:SS):")
        classificacao = input("Digite a classificação indicativa: ")

        conexaoDB = None
        cursor = None

        try:
            conexaoDB = psycopg.connect(
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT"),
                dbname=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                sslmode=os.getenv("DB_SSL")
            )
            cursor = conexaoDB.cursor()
            
            cursor.execute(f'''
            INSERT INTO filmes
            VALUES (default, %s, %s, %s);               
                            ''', (titulo, duracao, classificacao))
        
            conexaoDB.commit()
        
        except Exception as error:
            print("Erro no cadastro do filme")
            print(error)
            if (conexaoDB is not None):
                conexaoDB.rollback()            
        finally: 
            if (cursor is not None):
                cursor.close()
        
            if (conexaoDB is not None):
                conexaoDB.close

    elif (op == "4"):
        print("CADASTRAR NOVA SESSÃO")
        
        data = input("Digite a data (dd/mm/aa):")
        horario = input("Digite o horario (HH:MM:SS):")
        sala = int(input("Digite a sala: "))

        conexaoDB = None
        cursor = None

        try:
            conexaoDB = psycopg.connect(
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT"),
                dbname=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                sslmode=os.getenv("DB_SSL")
            )
            cursor = conexaoDB.cursor()
            
            cursor.execute(f'''
            INSERT INTO sessoes (cod_filme, data_sessao, horario_sessao, sala_sessao)
            VALUES (%s, %s, %s);               
                            ''', (data, horario, sala))
        
            conexaoDB.commit()
        
        except Exception as error:
            print("Erro no cadastro da sessão")
            print(error)
            if (conexaoDB is not None):
                conexaoDB.rollback()            
        finally: 
            if (cursor is not None):
                cursor.close()
        
            if (conexaoDB is not None):
                conexaoDB.close

    elif (op == "0"):
        print("Saindo do programa...")
        break
    else:
        print("Escolha uma opção válida...")
    
    input("TECLE ENTER PARA CONTINUAR")
    

        

            
        


