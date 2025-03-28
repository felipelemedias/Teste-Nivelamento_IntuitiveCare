import os
import requests
from bs4 import BeautifulSoup
import zipfile

def criar_pasta(destino: str):
    if not os.path.exists(destino):
        os.makedirs(destino)

def buscar_links_arquivos(url: str):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all("a", string=lambda text: text and 'Anexo' in text)

    pdf_links = []
    for link in links:
        href = link.get("href")
        if href and href.endswith(".pdf"):
            if not href.startswith("http"):
                href = f"https://www.gov.br{href}"
            pdf_links.append(href)

    return pdf_links[:2]  # Retorna apenas Anexo I e II

def baixar_arquivos(links, destino):
    nomes = ["Anexo_I.pdf", "Anexo_II.pdf"]
    caminhos = []

    for link, nome in zip(links, nomes):
        caminho = os.path.join(destino, nome)
        print(f"Baixando {nome}...")
        response = requests.get(link, stream=True)
        response.raise_for_status()

        with open(caminho, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"Salvo em: {caminho}")
        caminhos.append(caminho)

    return caminhos

def compactar_arquivos(arquivos, nome_zip):
    with zipfile.ZipFile(nome_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for arquivo in arquivos:
            zipf.write(arquivo, os.path.basename(arquivo))
            print(f"Adicionado ao ZIP: {os.path.basename(arquivo)}")

def main():
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    pasta_destino = "."
    nome_zip = os.path.join(pasta_destino, "anexos_compactados.zip")

    try:
        criar_pasta(pasta_destino)
        links = buscar_links_arquivos(url)
        arquivos = baixar_arquivos(links, pasta_destino)
        compactar_arquivos(arquivos, nome_zip)

        print("\nProcesso finalizado com sucesso!")
        print(f"Arquivos salvos em: {os.path.abspath(pasta_destino)}")
        print(f"ZIP criado: {os.path.abspath(nome_zip)}")

    except Exception as e:
        print(f"Erro durante o processo: {e}")

if __name__ == "__main__":
    main()
