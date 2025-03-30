import os
import pandas as pd
import zipfile
from exerc2 import (
    extrair_tabelas_pdf,
    limpar_e_transformar,
    salvar_csv,
    compactar_csv
)

# Caminho para o PDF original (vindo do exercício 1)
PDF_TEST_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'exercicio_1_WebScraping', 'Anexo_I.pdf')
)

def test_extrair_tabelas_pdf():
    dados = extrair_tabelas_pdf(PDF_TEST_PATH)
    assert isinstance(dados, list)
    assert len(dados) > 0  # Verifica que extraiu algo
    assert isinstance(dados[0], list)

def test_limpar_e_transformar():
    dados = [['Coluna1', 'Coluna2'], ['OD', 'AMB'], ['AMB', 'OD']]
    df = limpar_e_transformar(dados)
    assert isinstance(df, pd.DataFrame)
    assert df.iloc[0, 0] == 'Odontológico'
    assert df.iloc[0, 1] == 'Ambulatorial'

def test_salvar_csv(tmp_path):
    df = pd.DataFrame([{'A': 1, 'B': 2}])
    caminho = salvar_csv(df, tmp_path / 'teste.csv')
    assert os.path.exists(caminho)

def test_compactar_csv(tmp_path):
    # cria CSV falso
    csv_path = tmp_path / 'arquivo.csv'
    csv_path.write_text("coluna1;coluna2\n1;2", encoding='utf-8-sig')

    zip_path = compactar_csv(str(csv_path), tmp_path / 'arquivo.zip')
    assert os.path.exists(zip_path)

    with zipfile.ZipFile(zip_path, 'r') as zipf:
        assert 'arquivo.csv' in zipf.namelist()
