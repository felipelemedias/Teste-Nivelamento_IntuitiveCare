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

## 🧪 Testes com Postman

O projeto acompanha uma **coleção do Postman** (`Coleção 4. Teste API - IntuitiveCare.postman_collection.json`) que contém exemplos de requisições para testar a API com diferentes filtros (como CNPJ, UF, Representante, etc).

### Como importar a coleção no Postman:

1. Abra o Postman
2. Clique em **"Import"**
3. Selecione o arquivo `Coleção 4. Teste API - IntuitiveCare.postman_collection.json` dentro da pasta `back-end`
4. Execute as requisições da coleção com o backend em execução

---

## 📌 Observações

- A busca é realizada com base no arquivo `Relatorio_cadop.csv`
- Os campos disponíveis para busca são: `Razao_Social`, `Nome_Fantasia`, `CNPJ`, `Cidade`, `UF`, `Representante`
- A interface exibe os resultados de forma limpa e organizada, limitando os 10 mais relevantes

## 📌 Observação

Certifique-se de que o arquivo `Relatorio_cadop.csv` esteja dentro da pasta `Data/` para que o backend funcione corretamente.