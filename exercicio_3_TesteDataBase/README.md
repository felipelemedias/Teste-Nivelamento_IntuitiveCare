# Teste de Banco de dados

Crie scripts .sql que executem as tarefas abaixo:

## 📋 Pré-requisitos
- Postgres > 10


## ⚠️ AVISO ⚠️

Para a realização dessa tarefa, foram necessárias as seguintes modificações e ajustes nos dados:

1. **Inclusão do arquivo `relatorio_cadop_canceladas.csv`**:  
   Esse arquivo foi adicionado para incluir operadoras canceladas, pois os trimestres continham empresas que não estavam presentes no `relatorio_cadop`. Isso corrigiu inconsistências e permitiu o pleno funcionamento do script.

2. **Formatação de valores monetários**:  
   Todos os trimestres tiveram os valores monetários ajustados para usar `.` como separador decimal, em vez de `,`, para evitar problemas durante a importação.

3. **Exclusão do 4T2023**:  
   O trimestre 4T2023 foi ignorado devido a inconsistências nos dados, como mais de 20 mil linhas com `REG_ANS` inexistentes. Isso causava problemas na relação entre as tabelas `operadoras_ativas` e `demonstracoes_contabeis`.


## 🚀 Como usar

1. Extraia o conteúdo do arquivo `Data.zip` para um diretório acessível.

2. Utilize os comandos de criação de tabelas no arquivo `script.sql` para criar as tabelas no PostgreSQL.

3. Para inserir os dados, será necessário utilizar o terminal PSQL. Abra o terminal e conecte-se ao banco de dados(pgadmin, por exemplo) com o seguinte comando (substitua `usuario` e `nome_do_banco` pelos valores do seu ambiente):
```
psql -U usuario -d nome_do_banco
```

4. Nesse passo serão inseridas os dados das operadoras ativas e canceladas. No terminal PSQL, cole o primeiro comando e substitua o "seu_caminho_aqui" pelo caminho dos arquivos no primeiro substitua pelo caminho do arquivo Relatorio_cadop.csv, após isso repita o processo para o segundo e  substitua o X pelo caminho do Relatorio_cadop_canceladas.csv

No terminal PSQL, . Substitua X pelo caminho completo dos arquivos Relatorio_cadop.csv e Relatorio_cadop_canceladas.csv:

```
\COPY operadoras_ativas (
  registro_ans, cnpj, razao_social, nome_fantasia, modalidade,
  logradouro, numero, complemento, bairro, cidade, uf, cep, ddd, telefone,
  fax, email, representante, cargo_representante, regiao_de_comercializacao,
  data_registro_ans
) FROM 'seu_caminho_aqui\Relatorio_cadop.csv' WITH (FORMAT csv, DELIMITER ';', HEADER, ENCODING 'UTF8');


-- Canceladas
\COPY operadoras_ativas FROM 'seu_caminho_aqui\Relatorio_cadop_canceladas.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8';

```

5. Ainda no terminal PSQL, insira os dados trimestrais. Substitua "seu_caminho_aqui" pelo caminho completo de cada arquivo trimestral dentro da pasta Data. Não inclua o arquivo do 4T2023 (veja a explicação na seção ⚠️ AVISO ⚠️):

```
\COPY demonstracoes_contabeis FROM 'seu_caminho_aqui\1T2023.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8';


```

6. Agora basta realizar as querys que estão indicadas ao fim do script.

