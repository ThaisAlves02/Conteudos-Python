import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

conexao = None
cursor = None

try:
        conexao = psycopg.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            sslmode=os.getenv("DB_SSLMODE"),
        )
        cursor = conexao.cursor()

        cursor.execute("SELECT current_database(), CURRENT_DATE")
        linha = cursor.fetchone()
        print("Conectado! Resposta do banco:", linha)

        cursor.execute("DROP TABLE IF EXISTS filmes")
        cursor.execute("DROP TABLE IF EXISTS sessoes")


        cursor.execute("""
            CREATE TABLE filmes (
                cod_filme integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                titulo_filme varchar(100) NOT NULL,
                duracao_filme time NOT NULL,
                classificacao_filme char(2) NOT NULL,
                CONSTRAINT ck_duracao CHECK (duracao_filme > '00:00:00'),
                CONSTRAINT ck_classificacao CHECK (classificacao_filme IN ('L', '10', '12', '14', '16', '18'))
            )
        """)

        cursor.execute("""
            CREATE TABLE sessoes (
                cod_sessao integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                cod_filme integer NOT NULL,
                data_sessao date NOT NULL,
                horario_sessao time NOT NULL,
                sala_sessao integer NOT NULL,
                CONSTRAINT fk_sessoes_filmes FOREIGN KEY (cod_filme) REFERENCES filmes (cod_filme),
                CONSTRAINT ck_sala CHECK (sala_sessao BETWEEN 1 AND 5)
            )
        """)
        print("Tabelas criadas.")

        cursor.execute("""
            INSERT INTO filmes (titulo_filme, duracao_filme, classificacao_filme)
            VALUES 
                ('O Último Farol', '01:52:00', '12'),
                ('Corrida nas Dunas', '01:38:00', 'L'),
                ('Código Vermelho', '02:05:00', '16'),
                ('A Ilha dos Gatos', '01:38:00', 'L'),
                ('Noite sem Fim', '01:45:00', '14');
        """)

        cursor.execute("""
            INSERT INTO sessoes (cod_filme, data_sessao, horario_sessao, sala_sessao)
            VALUES 
                (1, '2026-11-06', '19:00:00', 1),
                (1, '2026-11-06', '21:30:00', 1),
                (2, '2026-11-07', '15:00:00', 2),
                (3, '2026-11-07', '20:00:00', 3),
                (4, '2026-11-08', '14:00:00', 2),
                (2, '2026-11-08', '16:30:00', 4);
        """)
        print("Dados inseridos.")

        conexao.commit()
        print("Banco Cinema Estrela pronto.")

except Exception as error:
    print(f"O tipo do erro foi: {type(error).__name__}")
    print(f"Mensagem do erro: {error}")

finally:
        if cursor is not None:
            cursor.close()

        if conexao is not None:
                    conexao.close()