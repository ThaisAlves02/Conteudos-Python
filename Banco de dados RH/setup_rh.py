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

        cursor.execute("DROP TABLE IF EXISTS funcionarios")
        cursor.execute("DROP TABLE IF EXISTS setores")

        cursor.execute("""
            CREATE TABLE setores (
                cod_setor integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                nome_setor varchar (60) NOT NULL UNIQUE
                )
        """)

        cursor.execute("""
                CREATE TABLE funcionarios (
                    cod_funcionario integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                    nome_funcionario varchar (100) NOT NULL,
                    cpf_funcionario char (11) NOT NULL UNIQUE,
                    cargo_funcionario varchar (60) NOT NULL,
                    salario_funcionario numeric (10,2) NOT NULL,
                    cod_setor integer NOT NULL,
                    CONSTRAINT ck_cpf_tamanho CHECK (LENGTH(cpf_funcionario) = 11),
                    CONSTRAINT ck_salario_funcionario CHECK (salario_funcionario > 0),
                    CONSTRAINT fk_func_setor FOREIGN KEY (cod_setor) REFERENCES setores (cod_setor)
                    )
        """)
        print("Tabelas criadas.")

        cursor.execute("""
            INSERT INTO setores (nome_setor)
            VALUES ('Administrativo'), ('Comercial'), ('Tecnologia')
        """)

        cursor.execute("""
            INSERT INTO funcionarios (nome_funcionario, cpf_funcionario, cargo_funcionario, salario_funcionario, cod_setor)
            VALUES ('Ana Souza', '12345678901', 'Analista de RH', 4200.00, 1),
                ('Bruno Lima', '09876543210', 'Vendedor', 3100.00, 2),
                ('Carla Mendes', '12365478900', 'Desenvolvedora', 6800.00, 3),
                ('Diego Rocha', '09846378190', 'Suporte técnico', 3500.00, 3),
                ('Elisa Martins', '12345678341', 'Gerente comercial', 7500.00, 2)
        """)
        print("Dados inseridos.")
        
        conexao.commit()
        print("Banco rh pronto.")
        

        while True:
            print("=== MENU RH ===")
            print("""
                    1. Ver funcionários
                    2. Ver departamentos
                    0. Sair
            """)
            op = input("Digite a opção desejada: ")

            if op == "1":
                print("Ver funcionários")
            elif op == "2":
                print("Ver departamentos")
            elif op == "0":
                print("Sair")
                break
            else:
                continue
            
except psycopg.OperationalError as erro:
       print("Não foi possível conectar ao banco.")
       print(erro)

finally:
        if cursor is not None:
            cursor.close()

        if conexao is not None:
                    conexao.close()