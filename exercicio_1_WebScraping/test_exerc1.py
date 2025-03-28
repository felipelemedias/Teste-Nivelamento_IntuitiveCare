# test_exerc1.py
import os
import zipfile
from exerc1 import criar_pasta, buscar_links_arquivos, compactar_arquivos

def test_criar_pasta(tmp_path):
    pasta = tmp_path / "nova_pasta"
    criar_pasta(str(pasta))
    assert pasta.exists()
    assert pasta.is_dir()

def test_buscar_links_arquivos():
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    links = buscar_links_arquivos(url)
    assert isinstance(links, list)
    assert len(links) == 2
    assert links[0].endswith(".pdf")

def test_compactar_arquivos(tmp_path):
    # Cria arquivos fictícios para zipar
    arq1 = tmp_path / "teste1.txt"
    arq2 = tmp_path / "teste2.txt"
    arq1.write_text("conteúdo 1")
    arq2.write_text("conteúdo 2")

    zip_path = tmp_path / "compactado.zip"
    compactar_arquivos([str(arq1), str(arq2)], str(zip_path))

    # Verifica se o ZIP foi criado corretamente
    assert zip_path.exists()
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        assert "teste1.txt" in zipf.namelist()
        assert "teste2.txt" in zipf.namelist()
