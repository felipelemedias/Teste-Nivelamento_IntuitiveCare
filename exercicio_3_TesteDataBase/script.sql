-- ========================================
-- SCRIPT DE BANCO DE DADOS - TESTE INTUITIVE CARE
-- Autor: Felipe (adaptado do layout oficial da ANS)
-- Banco: PostgreSQL >= 10
-- Objetivo: Criar estrutura, importar dados e realizar análises
-- ========================================

-- ===========================
-- 1. CRIAÇÃO DAS TABELAS
-- ===========================

-- Tabela de operadoras ativas cadastradas na ANS
DROP TABLE IF EXISTS demonstracoes_contabeis;
DROP TABLE IF EXISTS operadoras_ativas;

CREATE TABLE operadoras_ativas (
    registro_ans VARCHAR(20) PRIMARY KEY,
    cnpj VARCHAR(20),
    razao_social VARCHAR(255),
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(100),
    logradouro VARCHAR(255),
    numero VARCHAR(50),
    complemento VARCHAR(100),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf VARCHAR(2),
    cep VARCHAR(10),
    ddd VARCHAR(5),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    email VARCHAR(100),
    representante VARCHAR(255),
    cargo_representante VARCHAR(100),
    regiao_de_comercializacao INTEGER,
    data_registro_ans DATE,
    data_descredenciamento DATE,
    motivo_descredenciamento VARCHAR(255)
);

-- Tabela para armazenar demonstrações contábeis (últimos 2 anos)
CREATE TABLE demonstracoes_contabeis (
    id SERIAL PRIMARY KEY,
    data DATE,
    registro_ans VARCHAR(20),
    conta_contabil VARCHAR(100),
    descricao VARCHAR(255),
    vl_saldo_inicial DECIMAL(15,2),
    vl_saldo_final DECIMAL(15,2),
    FOREIGN KEY (registro_ans) REFERENCES operadoras_ativas(registro_ans)
);

-- ===========================
-- 2. IMPORTAÇÃO DOS DADOS
-- ===========================
-- Execute os comandos abaixo no terminal PSQL:
-- psql -U seu_usuario -d nome_do_banco

-- IMPORTAR DADOS DAS OPERADORAS
-- (substitua o caminho completo corretamente)

-- Ativas
\COPY operadoras_ativas (
  registro_ans, cnpj, razao_social, nome_fantasia, modalidade,
  logradouro, numero, complemento, bairro, cidade, uf, cep, ddd, telefone,
  fax, email, representante, cargo_representante, regiao_de_comercializacao,
  data_registro_ans
) FROM 'C:\Users\fleme\OneDrive\Documentos\TesteNivelamento_IntuitiveCare\exercicio_3_TesteDataBase\Data\Relatorio_cadop.csv' WITH (FORMAT csv, DELIMITER ';', HEADER, ENCODING 'UTF8');

-- Canceladas
\COPY operadoras_ativas FROM 'C:\Users\fleme\OneDrive\Documentos\TesteNivelamento_IntuitiveCare\exercicio_3_TesteDataBase\Data\Relatorio_cadop_canceladas.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8';

-- DADOS CONTÁBEIS
-- (Ignorar 4T2023 por inconsistência dos dados)
\COPY demonstracoes_contabeis FROM 'C:\Users\fleme\OneDrive\Documentos\TesteNivelamento_IntuitiveCare\exercicio_3_TesteDataBase\Data\1T2023.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8';
\COPY demonstracoes_contabeis FROM 'C:\Users\fleme\OneDrive\Documentos\TesteNivelamento_IntuitiveCare\exercicio_3_TesteDataBase\Data\2T2023.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8';
\COPY demonstracoes_contabeis FROM 'C:\Users\fleme\OneDrive\Documentos\TesteNivelamento_IntuitiveCare\exercicio_3_TesteDataBase\Data\3T2023.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8';
\COPY demonstracoes_contabeis FROM 'C:\Users\fleme\OneDrive\Documentos\TesteNivelamento_IntuitiveCare\exercicio_3_TesteDataBase\Data\1T2024.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8';
\COPY demonstracoes_contabeis FROM 'C:\Users\fleme\OneDrive\Documentos\TesteNivelamento_IntuitiveCare\exercicio_3_TesteDataBase\Data\2T2024.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8';
\COPY demonstracoes_contabeis FROM 'C:\Users\fleme\OneDrive\Documentos\TesteNivelamento_IntuitiveCare\exercicio_3_TesteDataBase\Data\3T2024.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8';
\COPY demonstracoes_contabeis FROM 'C:\Users\fleme\OneDrive\Documentos\TesteNivelamento_IntuitiveCare\exercicio_3_TesteDataBase\Data\4T2024.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8';

-- ===========================
-- 3. CONSULTAS ANALÍTICAS
-- ===========================

-- 3.5.a) Top 10 operadoras com maiores despesas em "EVENTOS/SINISTROS..." no último trimestre
SELECT 
    o.razao_social,
    o.nome_fantasia,
    o.uf,
    SUM(d.vl_saldo_final - d.vl_saldo_inicial) AS total_despesas
FROM 
    demonstracoes_contabeis d
JOIN 
    operadoras_ativas o ON d.registro_ans = o.registro_ans
WHERE 
    (d.descricao ILIKE '%Despesas com Eventos / Sinistros%' OR
     d.descricao ILIKE '%AVISADOS DE ASSISTENCIA A SAUDE MEDICO HOSPITALAR%' OR
     d.descricao ILIKE '%EVENTOS/SINISTROS CONHECIDOS%')
    AND d.data >= DATE_TRUNC('quarter', CURRENT_DATE) - INTERVAL '3 months'
    AND d.data < DATE_TRUNC('quarter', CURRENT_DATE)
GROUP BY 
    o.razao_social, o.nome_fantasia, o.uf
HAVING 
    SUM(d.vl_saldo_final - d.vl_saldo_inicial) > 0
ORDER BY 
    total_despesas DESC
LIMIT 10;

-- 3.5.b) Top 10 operadoras com maiores despesas nessa categoria no último ano
SELECT 
    o.razao_social,
    o.nome_fantasia,
    o.uf,
    SUM(d.vl_saldo_final - d.vl_saldo_inicial) AS total_despesas_anual
FROM 
    demonstracoes_contabeis d
JOIN 
    operadoras_ativas o ON d.registro_ans = o.registro_ans
WHERE 
    (d.descricao ILIKE '%Despesas com Eventos / Sinistros%' OR
     d.descricao ILIKE '%AVISADOS DE ASSISTENCIA A SAUDE MEDICO HOSPITALAR%' OR
     d.descricao ILIKE '%EVENTOS/SINISTROS CONHECIDOS%')
    AND d.data >= CURRENT_DATE - INTERVAL '1 year'
GROUP BY 
    o.razao_social, o.nome_fantasia, o.uf
HAVING 
    SUM(d.vl_saldo_final - d.vl_saldo_inicial) > 0
ORDER BY 
    total_despesas_anual DESC
LIMIT 10;
