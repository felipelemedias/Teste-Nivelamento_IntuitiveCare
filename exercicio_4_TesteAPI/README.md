# 🚀 Projeto - Teste de API com FastAPI + Vue.js

Este projeto tem como objetivo realizar buscas em uma base de dados de operadoras de saúde, utilizando backend em **FastAPI (Python)** e frontend em **Vue.js (Vite)**.

---

## 📁 Estrutura de Pastas

```
exercicio_4_TesteAPI/
├── backend/           # Backend FastAPI
│   ├── server.py      # Código principal do servidor
│   ├── Data/          # Contém o arquivo CSV
│   ├── venv/          # Ambiente virtual Python
│   └── requirements.txt
└── frontend/          # Aplicação Vue.js
    └── src/
        ├── App.vue    # Componente principal
        └── main.js
```

---

## ⚙️ Requisitos

- Python 3.10+
- Node.js 16+
- npm ou yarn

---

## ▶️ Como rodar o projeto

### 🔹 1. Clonar o repositório (se ainda não tiver)

```bash
git clone https://github.com/felipelemedias/Teste-Nivelamento_IntuitiveCare
cd exercicio_4_TesteAPI
```

---

### 🔹 2. Backend (FastAPI)

#### a) Entrar na pasta `backend`:
```bash
cd backend
```

#### b) Criar e ativar o ambiente virtual:

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### c) Instalar dependências:
```bash
pip install -r requirements.txt
```

#### d) Rodar o servidor:
```bash
uvicorn server:app --reload
```

> O backend será iniciado em: [http://localhost:8000](http://localhost:8000)

---

### 🔹 3. Frontend (Vue.js)

#### a) Entrar na pasta `front-end`:
```bash
cd front-end
```

#### b) Instalar as dependências:
```bash
npm install
```

#### c) Rodar o frontend:
```bash
npm run dev
```

> O frontend será iniciado em: [http://localhost:5173](http://localhost:5173)

---

## 📌 Observações

- O back-end carrega o arquivo `Relatorio_cadop.csv` para realizar as buscas.
- A busca pode ser feita por Razão Social, Nome Fantasia, CNPJ, Cidade, UF e Representante.
- A interface exibe os resultados de forma limpa e organizada.

---

## 💡 Dica

Caso altere a porta do back-end ou front-end, ajuste os endpoints no código do Vue (por padrão está apontando para `http://localhost:8000`).

---