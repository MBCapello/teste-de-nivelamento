from transformacao_dados.extract_pdf import extract_data
from transformacao_dados.transform_pdf_to_csv import transform_data_to_csv
from transformacao_dados.compact_csv import compact_csv

if __name__ == "__main__":
    extracted_data = extract_data()
    if extracted_data:
        print(f"Dados extraídos: {len(extracted_data)} registros encontrados.")
        # Defina o caminho do CSV para salvar os dados
        csv_path = 'output/Tabela_anexo_I.csv'
        transform_data_to_csv(extracted_data, csv_path)
        
        # Compacta o arquivo CSV gerado
        zip_path = 'output/Teste_Marcelo_Capello.zip'
        compact_csv(csv_path, zip_path)
    else:
        print("Nenhum dado extraído.")
