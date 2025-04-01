import os
import requests
import tqdm
from .scraper import get_pdf_links

# Garante que o download_folder seja um caminho absoluto e esteja correto.
download_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "../output/download"))

def pdf_downloader(pdf_links, save_path=download_folder):
    """
    Baixa arquivos PDF de uma lista de URLs e os salva em um diretório especificado.
    """

    try:
        os.makedirs(save_path, exist_ok=True)  # Cria o diretório se ele não existir
    except OSError as e:
        print(f"Erro ao criar o diretório {save_path}: {e}")
        return  # Interrompe o download se o diretório não puder ser criado

    for pdf in pdf_links:
        pdf_name = os.path.join(save_path, pdf.split("/")[-1])  # Obtém o nome do arquivo da URL
        try:
            response = requests.get(pdf, stream=True)  # Faz a requisição HTTP com streaming
            response.raise_for_status()  # Lança uma exceção para erros HTTP (4xx ou 5xx)

            content_type = response.headers.get("Content-Type")  # Obtém o tipo de conteúdo do cabeçalho
            if "application/pdf" not in content_type:
                print(f"Conteúdo inválido (não é PDF) para {pdf_name}, Content-Type: {content_type}")
                continue  # Pula para o próximo PDF se o conteúdo não for PDF

            with open(pdf_name, "wb") as file:  # Abre o arquivo para escrita binária
                for chunk in tqdm.tqdm(response.iter_content(chunk_size=1024), unit="KB", unit_scale=True, desc=f"Baixando {pdf_name}"):
                    file.write(chunk)  # Escreve cada parte (chunk) do arquivo

            print(f"{pdf_name} baixado com sucesso!")

        except requests.exceptions.RequestException as e:
            print(f"Erro ao baixar {pdf_name}: {e}")  # Trata erros de requisição HTTP
        except Exception as e:
            print(f"Erro inesperado ao baixar {pdf_name}: {e}")  # Trata outros erros

    print("Download concluído!")

if __name__ == "__main__":
    pdf_downloader(get_pdf_links())