# 🧪 Teste de Nivelamento - IntuitiveCare

Este repositório contém a solução completa para o **teste técnico de nivelamento** proposto pela IntuitiveCare.  
Os desafios abordam **web scraping, tratamento de dados, banco de dados e desenvolvimento de APIs com frontend.**

---

## 📁 Estrutura do Projeto

```
Teste-Nivelamento_IntuitiveCare/
├── exercicio_1_WebScraping/       → Download e compactação de PDFs via scraping
├── exercicio_2_TransformarDados/  → Leitura e estruturação dos dados extraídos do PDF
├── exercicio_3_TesteDataBase/     → Criação de banco de dados com script SQL e comando PSQL
├── exercicio_4_TesteAPI/          → Backend (FastAPI) e Frontend (Vue.js)
```

---

## 🧠 Descrição dos Exercícios

### ✅ **Exercício 1 - WebScraping**
- Acessa o site da ANS.
- Busca e baixa os arquivos PDF “Anexo I” e “Anexo II”.
- Salva localmente e compacta os arquivos em `.zip`.

### ✅ **Exercício 2 - Transformar Dados**
- Lê os dados do PDF baixado.
- Converte para estrutura tabular.
- Exporta para CSV com os dados tratados.

### ✅ **Exercício 3 - Teste com Banco de Dados**
- Criação de um banco relacional baseado no CSV anterior.
- Arquivo `.sql` com `CREATE TABLE` e inserts simulados.

### ✅ **Exercício 4 - API e Frontend**
- Backend: FastAPI que busca registros com base na relevância do termo buscado.
- Frontend: Vue.js com Vite para busca dinâmica por Razão Social, CNPJ, Cidade etc.
- Comunicação entre frontend e backend via fetch API.

---

## 🚀 Como Clonar e Executar o Projeto


### 1. Clone o repositório
```bash
git clone https://github.com/felipelemedias/Teste-Nivelamento_IntuitiveCare
cd Teste-Nivelamento_IntuitiveCare
```

2. Navegue até o exercício desejado e siga o passo a passo descrito no seu `README.md`.

---

## ⚙️ Como executar

Cada exercício pode ser executado individualmente.  
Basta seguir as instruções no `README.md` presente em **cada pasta** do projeto.

- Os ambientes (Python, Node.js) estão separados por exercício
- As dependências estão listadas em `requirements.txt` ou `package.json`
- O projeto não exige nenhum serviço externo além dos comandos descritos

---

### 🔹 Ex. 1 e 2 (Python)
```bash
cd exercicio_1_WebScraping  # ou exercicio_2_TransformarDados
python -m venv venv
venv\Scripts\activate      # Windows
pip install -r requirements.txt
python exerc1.py             # ou exerc2.py
```

### 🔹 Ex. 3 (SQL)
Abra o arquivo `script.sql` com o gerenciador de banco (ex: MySQL Workbench, DBeaver)  
e execute o script para criar as tabelas e carregar os dados.

### 🔹 Ex. 4 (API + Frontend)

#### Backend (FastAPI):
```bash
cd exercicio_4_TesteAPI/backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn server:app --reload
```

#### Frontend (Vue.js):
```bash
cd ../frontend
npm install
npm run dev
```

---

## 📜 Licença

Este projeto está sob a licença MIT. Veja o arquivo [`LICENSE`](./LICENSE) para mais detalhes.

---

Desenvolvido por **Felipe Leme Dias**, 2025.