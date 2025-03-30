import os
import zipfile
from tqdm import tqdm

output_folder = "output" #Definindo a pasta output.

def zip_files_from_directory(directory_path, output_zip):
    """Compacta todos os arquivos em um diretório em um arquivo ZIP com barra de progresso."""

    file_paths = [os.path.join(directory_path, filename) for filename in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, filename))]

    with zipfile.ZipFile(output_zip, 'w') as zipf:
        for file_path in tqdm(file_paths, desc="Compactando arquivos"):
            zipf.write(file_path, os.path.basename(file_path))

if __name__ == "__main__":
    from downloader import download_folder
    os.makedirs(output_folder, exist_ok=True) #Cria a pasta output caso não exista.
    output_zip = os.path.join(output_folder, "arquivos_compactados.zip")
    zip_files_from_directory(download_folder, output_zip)
    print(f"Arquivos compactados em {output_zip}")