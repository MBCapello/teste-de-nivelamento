# main.py
from web_scraping.scraper import get_pdf_links
from web_scraping.downloader import pdf_downloader, download_folder
from web_scraping.zipper import zip_files_from_directory
import os

output_folder = "output"

def main():
    pdf_links = get_pdf_links()
    if pdf_links:
        pdf_downloader(pdf_links)
        os.makedirs(output_folder, exist_ok=True) #Cria a pasta output caso não exista.
        zip_files_from_directory(download_folder, os.path.join(output_folder, "arquivos_compactados.zip"))
        print("Processo concluído!")
    else:
        print("Nenhum link de PDF encontrado.")

if __name__ == "__main__":
    main()