import zipfile
import os

def compact_csv(csv_path, zip_path):
    """
    Compacta um arquivo CSV em um arquivo ZIP.
    """
    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(csv_path, os.path.basename(csv_path))
        print(f"Arquivo CSV compactado em {zip_path}")
    except FileNotFoundError:
        print(f"Arquivo CSV não encontrado: {csv_path}")
    except Exception as erro:
        print(f"Erro ao compactar arquivo CSV: {erro}")

if __name__ == "__main__":
    csv_path = 'output/Tabela_anexo_I.csv'
    zip_path = 'output/Teste_Marcelo_Capello.zip'
    compact_csv(csv_path, zip_path)
