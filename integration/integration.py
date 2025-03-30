import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from web_scraping.scraper import get_pdf_links
from web_scraping.downloader import pdf_downloader, download_folder
from web_scraping.zipper import zip_files_from_directory

output_folder = "output"

def integrate_web_scraping():
    """Integra os módulos web_scraping."""

    pdf_links = get_pdf_links("https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos")
    pdf_downloader(pdf_links)
    os.makedirs(output_folder, exist_ok=True) #Cria a pasta output caso não exista.
    zip_files_from_directory(download_folder, os.path.join(output_folder, "arquivos_compactados.zip"))

def main():
    integrate_web_scraping()
    print("Integração concluída!")

if __name__ == "__main__":
    main()