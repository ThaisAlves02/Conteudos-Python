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
                cod_filme integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                titulo_filme varchar(100) NOT NULL,
                duracao_filme time NOT NULL,
                CONSTRAINT ck_ CHECK (LENGTH(cpf_funcionario) = 11)
        """)
except:
        pass