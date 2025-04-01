import pdfplumber
import os
from web_scraping.downloader import download_folder
from tqdm import tqdm

def extract_data():
    """Extrai dados de tabelas dos PDFs do Anexo I."""
    pdf_files = [pdf for pdf in os.listdir(download_folder) 
                 if pdf.endswith('.pdf') and 'Anexo_I' in pdf and 'Anexo_II' not in pdf]
    
    if not pdf_files:
        print("Nenhum PDF encontrado no diretório especificado.")
        return []

    all_data = []

    for pdf in tqdm(pdf_files, desc="Extraindo dados do Anexo I"):
        pdf_path = os.path.join(download_folder, pdf)
        try:
            with pdfplumber.open(pdf_path) as pdf_file:
                for page in pdf_file.pages:
                    tables = page.extract_tables()
                    if not tables:
                        print(f"Nenhuma tabela encontrada na página {page.page_number} do arquivo {pdf}")
                        print("Por favor aguarde...")
                        continue
                    
                    for table in tables:
                        if not table or len(table) < 2:
                            print(f"Tabela vazia ou sem estrutura válida no PDF {pdf}, página {page.page_number}")
                            continue
                        
                        headers = table[0]  # Assume que a primeira linha são os cabeçalhos
                        for row in table[1:]:
                            if len(row) != len(headers):  # Evita desalinhamento de colunas
                                print(f"Erro de alinhamento de colunas na página {page.page_number} do PDF {pdf}")
                                continue
                            row_data = dict(zip(headers, row))
                            all_data.append(row_data)

        except Exception as erro:
            print(f"Erro ao extrair dados do PDF {pdf}: {erro}")

    return all_data
