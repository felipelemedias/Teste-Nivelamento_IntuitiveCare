import os
import pdfplumber
import pandas as pd
import zipfile

def extrair_tabelas_pdf(pdf_path: str):
    dados = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tabelas = page.extract_tables()
            for tabela in tabelas:
                if tabela:
                    dados.extend(tabela)
    return dados

def limpar_e_transformar(dados: list):
    df = pd.DataFrame(dados[1:], columns=dados[0])
    df.dropna(axis=1, how='all', inplace=True)
    df.columns = df.columns.str.replace('\n', ' ', regex=True).str.strip()
    df.replace({'OD': 'Odontológico', 'AMB': 'Ambulatorial'}, inplace=True)
    df.dropna(how='all', inplace=True)
    return df

def salvar_csv(df: pd.DataFrame, nome_csv: str):
    caminho_csv = os.path.join(os.path.dirname(__file__), nome_csv)
    df.to_csv(caminho_csv, index=False, sep=';', encoding='utf-8-sig')
    return caminho_csv

def compactar_csv(caminho_csv: str, nome_zip: str):
    caminho_zip = os.path.join(os.path.dirname(__file__), nome_zip)
    with zipfile.ZipFile(caminho_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(caminho_csv, os.path.basename(caminho_csv))
    return caminho_zip

def main():
    BASE_DIR = os.path.dirname(__file__)
    pdf_path = os.path.abspath(os.path.join(BASE_DIR, '..', 'exercicio_1_WebScraping', 'Anexo_I.pdf'))
    nome_csv = 'RolProcedimentos&Eventos_Estruturados.csv'
    nome_zip = 'Teste_Felipe.zip'
    print(pdf_path)

    try:
        print("Extraindo tabelas do PDF...")
        dados_extraidos = extrair_tabelas_pdf(pdf_path)

        print("Transformando e limpando dados...")
        df = limpar_e_transformar(dados_extraidos)

        print("Salvando CSV...")
        caminho_csv = salvar_csv(df, nome_csv)

        print("Compactando arquivo CSV...")
        caminho_zip = compactar_csv(caminho_csv, nome_zip)

        print("\nTransformação e estruturação concluídas com sucesso!")
        print(f"CSV salvo em: {caminho_csv}")
        print(f"ZIP criado em: {caminho_zip}")

    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

if __name__ == "__main__":
    main()
    