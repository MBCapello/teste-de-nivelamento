import os
import zipfile
from web_scraping.zipper import zip_files_from_directory

def test_zip_files_from_directory(tmp_path):
    """Testa a função zip_files_from_directory."""

    file_paths = [tmp_path / "arquivo1.txt", tmp_path / "arquivo2.txt"]
    for file_path in file_paths:
        file_path.write_text("Conteúdo de teste")

    output_zip = tmp_path / "arquivos_compactados.zip"
    zip_files_from_directory(str(tmp_path), str(output_zip))

    assert os.path.exists(output_zip)
    with zipfile.ZipFile(output_zip, 'r') as zipf:
        assert len(zipf.namelist()) == 2
        assert "arquivo1.txt" in zipf.namelist()
        assert "arquivo2.txt" in zipf.namelist()