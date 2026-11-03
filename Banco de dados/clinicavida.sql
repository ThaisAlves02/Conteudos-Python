-- 1) CRIAR O BANCO DE DADOS DA CLINICA
-- CREATE DATABASE clinica;

-- 2) Apagar: filhos antes dos pais
DROP TABLE IF EXISTS consultas;
DROP TABLE IF EXISTS convenios;
DROP TABLE IF EXISTS medicos;
DROP TABLE IF EXISTS pacientes;

-- 3) Criar: pais antes dos filhos
-- 1. Criar primeiro as tabelas independentes ou que são referenciadas
CREATE TABLE convenios (
    cod_conv integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome_conv varchar (255) NOT NULL,
    fone_conv varchar(20) DEFAULT 'N/A'
);

CREATE TABLE medicos (
    cod_med integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    crm_med char(5) NOT NULL, -- Corrigido para crm_med
    nome_med varchar (255) NOT NULL,
    especialidade_med varchar (255) NOT NULL
);

-- 2. Criar tabelas com chaves estrangeiras
CREATE TABLE pacientes (
    cod_pac integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome_pac varchar (255) NOT NULL,
    cpf_pac char(11) NOT NULL,
    fone_pac varchar(20) DEFAULT 'N/A',
    cod_conv integer, -- Adicionado: coluna que estava faltando
    CONSTRAINT fk_pacientes_convenios FOREIGN KEY (cod_conv) REFERENCES convenios(cod_conv)
);

CREATE TABLE consultas (
    cod_cons integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    data_cons date,
    hora_cons time,
    diagnostico_cons varchar (255), -- Removido o NOT NULL para aceitar os valores nulos da imagem
    cod_pac integer NOT NULL,
    cod_med integer NOT NULL,
    CONSTRAINT fk_consultas_pacientes FOREIGN KEY (cod_pac) REFERENCES pacientes(cod_pac),
    CONSTRAINT fk_consultas_medicos FOREIGN KEY (cod_med) REFERENCES medicos(cod_med)
);

-- CONVENIOS
INSERT INTO convenios (nome_conv, fone_conv) VALUES ('Saúde Total', '(85) 3333-1000');
INSERT INTO convenios (nome_conv, fone_conv) VALUES ('Vida Mais', '(85) 3333-2000');
INSERT INTO convenios (nome_conv, fone_conv) VALUES ('Bem Estar', '(85) 3333-3000');

-- MEDICOS
INSERT INTO medicos (crm_med, nome_med, especialidade_med) VALUES ('12345', 'Helena Duarte', 'Cardiologia');
INSERT INTO medicos (crm_med, nome_med, especialidade_med) VALUES ('23456', 'Otávio Nunes', 'Clínica Geral');
INSERT INTO medicos (crm_med, nome_med, especialidade_med) VALUES ('34567', 'Sofia Brandão', 'Dermatologia');
INSERT INTO medicos (crm_med, nome_med, especialidade_med) VALUES ('45678', 'Caio Ferraz', 'Ortopedia');

-- PACIENTES
INSERT INTO pacientes (nome_pac, cpf_pac, fone_pac, cod_conv) VALUES ('Marina Alves', '10120230344', '(85) 98888-0001', 1);
INSERT INTO pacientes (nome_pac, cpf_pac, fone_pac, cod_conv) VALUES ('João Pedro Lins', '20230340455', '(85) 98888-0002', 2);
INSERT INTO pacientes (nome_pac, cpf_pac, fone_pac, cod_conv) VALUES ('Beatriz Sales', '30340450566', '(85) 98888-0003', 1);
INSERT INTO pacientes (nome_pac, cpf_pac, fone_pac, cod_conv) VALUES ('Renato Dias', '40450560677', '(85) 98888-0004', 2);
INSERT INTO pacientes (nome_pac, cpf_pac, fone_pac, cod_conv) VALUES ('Clara Nogueira', '50560670788', '(85) 98888-0005', 1);

-- CONSULTAS
INSERT INTO consultas (data_cons, hora_cons, diagnostico_cons, cod_pac, cod_med) VALUES ('2026-10-05', '08:00', 'Hipertensão leve', 1, 1);
INSERT INTO consultas (data_cons, hora_cons, diagnostico_cons, cod_pac, cod_med) VALUES ('2026-10-05', '09:00', 'Virose', 2, 2);
INSERT INTO consultas (data_cons, hora_cons, diagnostico_cons, cod_pac, cod_med) VALUES ('2026-10-06', '14:00', 'Dermatite', 3, 3);
INSERT INTO consultas (data_cons, hora_cons, diagnostico_cons, cod_pac, cod_med) VALUES ('2026-10-07', '10:00', 'Alergia de contato', 1, 3);
INSERT INTO consultas (data_cons, hora_cons, diagnostico_cons, cod_pac, cod_med) VALUES ('2026-10-27', '08:00', NULL, 4, 1);
INSERT INTO consultas (data_cons, hora_cons, diagnostico_cons, cod_pac, cod_med) VALUES ('2026-10-27', '15:00', NULL, 2, 1);
INSERT INTO consultas (data_cons, hora_cons, diagnostico_cons, cod_pac, cod_med) VALUES ('2026-10-28', '09:30', NULL, 4, 3);