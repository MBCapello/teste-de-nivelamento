import sys
import os
import logging

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from web_scraping.scraper import get_pdf_links
from web_scraping.downloader import pdf_downloader, download_folder
from web_scraping.zipper import zip_files_from_directory
from transformacao_dados.extract_pdf import extract_data
from transformacao_dados.transform_pdf_to_csv import transform_data_to_csv
from transformacao_dados.compact_csv import compact_csv
from banco_dados.demonstrativos_importer import import_demonstrativos
from banco_dados.operadoras_importer import import_operadoras
from banco_dados.top_10_despesas import top_10_despesas
from banco_dados.create_schema import create_schema

# Diretório de saída
output_folder = "output"

# Configuração básica de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def integrate_web_scraping():
    """Integra os módulos web_scraping."""
    try:
        pdf_links = get_pdf_links("https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos")
        pdf_downloader(pdf_links)
        os.makedirs(output_folder, exist_ok=True)
        zip_files_from_directory(download_folder, os.path.join(output_folder, "arquivos_compactados.zip"))
        logging.info("Integração web_scraping concluída!")
    except Exception as e:
        logging.error(f"Erro na integração web_scraping: {e}")

def integrate_transformacao_dados():
    """Integra os módulos transformacao_dados."""
    try:
        extracted_data = extract_data()
        if extracted_data:
            csv_path = os.path.join(output_folder, 'Tabela_anexo_I.csv')
            transform_data_to_csv(extracted_data, csv_path)
            zip_path = os.path.join(output_folder, 'Teste_Marcelo_Capello.zip')
            compact_csv(csv_path, zip_path)
            logging.info("Integração transformacao_dados concluída!")
        else:
            logging.warning("Aviso: Nenhum dado do Anexo I encontrado.")
    except Exception as e:
        logging.error(f"Erro na integração transformacao_dados: {e}")

def create_database_schema():
    """Cria o esquema do banco de dados."""
    try:
        connection, cursor = create_schema()
        if connection and cursor:
            logging.info("Esquema do banco de dados criado com sucesso!")
            return connection, cursor
        else:
            logging.error("Erro ao criar o esquema do banco de dados.")
            return None, None
    except Exception as e:
        logging.error(f"Erro ao criar o esquema do banco de dados: {e}")
        return None, None

def integrate_banco_dados():
    """Integra o módulo banco_dados."""
    try:
        connection, cursor = create_database_schema()
        if connection and cursor:
            operadoras_path = 'data/operadoras/Relatorio_cadop.csv'
            demonstrativos_path = 'data/demonstrativos'
            import_operadoras(operadoras_path)
            import_demonstrativos(demonstrativos_path)
            logging.info("Dados importados para o banco de dados com sucesso!")

            # Executa as queries do top_10_despesas
            top_10_despesas()

            cursor.close()
            connection.close()
        else:
            logging.error("Conexão com o banco de dados falhou.")
    except Exception as e:
        logging.error(f"Erro na integração banco_dados: {e}")

def main():
    """Função principal para executar todas as integrações."""
    logging.info("Iniciando o processo de integração...")
    integrate_web_scraping()
    integrate_transformacao_dados()
    integrate_banco_dados()
    logging.info("Processo de integração completo!")

if __name__ == "__main__":
    main()