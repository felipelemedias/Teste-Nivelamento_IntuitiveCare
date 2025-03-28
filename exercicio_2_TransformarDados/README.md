# Transformação e Estruturação de Dados do Anexo I

Script Python para extrair tabelas do PDF "Anexo I", transformar e limpar os dados, salvar em um arquivo CSV e compactá-lo em um arquivo ZIP.

## 📋 Pré-requisitos
- Python 3.0+
- Bibliotecas listadas em `requirements.txt`

## 🛠 Instalação

1. Criar ambiente virtual:

    **Caso o SO seja WINDOWS:**
    ```bash
    python3 -m venv venv
    ```
    Em seguida use:
    ```bash
    venv\Scripts\activate
    ```

    Em caso de problemas de segurança do Powershell, execute o powershell como administrador e digite o comando: 
    ```
    Set-ExecutionPolicy RemoteSigned
    ```

    Depois, tente criar o VENV novamente.

    **Caso o SO seja LINUX:**
    ```bash
    python3 -m venv venv

    chmod +x ./venv/bin/activate

    source venv/bin/activate
    ```

2. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Como usar

Execute o script com o seguinte comando no console:
```bash
python exerc2.py