# 🛠️ Backend - FastAPI

Este diretório contém o backend da aplicação, desenvolvido com **FastAPI**.

---

## ▶️ Como rodar o backend

### 1. Entrar na pasta `back-end`:
```bash
cd back-end
```

### 2. Criar e ativar o ambiente virtual:

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

### 3. Instalar as dependências:
```bash
pip install -r requirements.txt
```

### 4. Rodar o servidor:
```bash
uvicorn server:app --reload
```

### 4. Rodar o servidor pelo arquivo server.py (cenário alternativo caso o passo 4 dê erro):
```bash
python server.py
```

> O servidor será iniciado em: [http://localhost:8000](http://localhost:8000)

---

## 📂 Estrutura

- `server.py` → Código principal da API
- `Data/Relatorio_cadop.csv` → Base de dados usada para busca
- `requirements.txt` → Bibliotecas necessárias

---

## 🔎 Endpoint principal

### `/buscar`

**Método:** `GET`  
**Parâmetros:**
- `campo`: campo da base para busca (ex: `Razao_Social`, `Cidade`, etc)
- `termo`: termo que será buscado no campo

**Exemplo:**
```
/buscar?campo=Razao_Social&termo=UNIMED
```

**Retorno:** JSON com até 10 operadoras mais relevantes.

---

## 📌 Observação

Certifique-se de que o arquivo `Relatorio_cadop.csv` esteja dentro da pasta `Data/` para que o backend funcione corretamente.