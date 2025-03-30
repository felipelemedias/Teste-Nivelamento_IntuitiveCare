from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# Libera CORS para o frontend acessar
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Carregamento inicial do CSV
CAMINHO_ARQUIVO = "Data/Relatorio_cadop.csv"
df_original = pd.read_csv(CAMINHO_ARQUIVO, sep=";", encoding="UTF-8")

# Configurações da busca
COLUNAS_BUSCA = [
    "Razao_Social", "CNPJ", "Nome_Fantasia", "Modalidade", "Logradouro", 
    "Numero", "Complemento", "Bairro", "Cidade", "UF", "CEP", "DDD", 
    "Telefone", "Fax", "Endereco_eletronico", "Representante", 
    "Cargo_Representante", "Regiao_de_Comercializacao", "Data_Registro_ANS"
]

PESOS_COLUNAS = {
    "CNPJ": 30,
    "Razao_Social": 25,
    "Nome_Fantasia": 20,
    "Cidade": 15,
    "UF": 12,
    "Regiao_de_Comercializacao": 10,
    "Logradouro": 8,
    "Bairro": 6,
    "CEP": 5,
    "Telefone": 7,
    "Endereco_eletronico": 6,
    "DDD": 4,
    "Fax": 3,
    "Representante": 5,
    "Cargo_Representante": 2,
    "Modalidade": 4,
    "Complemento": 3,
    "Numero": 2,
    "Data_Registro_ANS": 1
}

CAMPOS_RESPOSTA = [
    "Razao_Social", "CNPJ", "Nome_Fantasia", "Modalidade",
    "Cidade", "UF", "Telefone", "Endereco_eletronico", "Representante"
]

BONUS_EXATO = 10
LIMITE_RESULTADOS = 10

@app.get("/buscar")
def buscar_operadoras(
    campo: str = Query(..., description="Campo a ser buscado"),
    termo: str = Query(..., description="Valor a ser buscado")
):
    if campo not in COLUNAS_BUSCA:
        return {"erro": f"Campo '{campo}' não é válido."}

    df = df_original.copy()
    df[campo] = df[campo].astype(str)

    contem_termo = df[campo].str.contains(termo, case=False, na=False)
    match_exato = df[campo].str.lower() == termo.strip().lower()

    df["relevancia"] = 0
    df.loc[contem_termo, "relevancia"] += PESOS_COLUNAS.get(campo, 1)
    df.loc[match_exato, "relevancia"] += BONUS_EXATO

    df_resultado = df[df["relevancia"] > 0].sort_values("relevancia", ascending=False)

    return (
    df_resultado[CAMPOS_RESPOSTA]
    .head(LIMITE_RESULTADOS)
    .replace({float('inf'): None, float('-inf'): None})
    .fillna("")
    .to_dict(orient="records")
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
