from unittest.mock import patch, MagicMock
from transformacao_dados.compact_csv import compact_csv
import zipfile

def test_compact_csv():
    """Testa a função compact_csv."""
    csv_path = 'test.csv'
    zip_path = 'test.zip'

    with patch("transformacao_dados.compact_csv.zipfile.ZipFile") as mock_zip:
        # Cria o mock para o ZipFile
        mock_zip.return_value.__enter__.return_value = MagicMock()

        # Chama a função de compactação
        compact_csv(csv_path, zip_path)

        # Verifica se o método de criação do zip foi chamado corretamente
        mock_zip.assert_called_once_with(zip_path, 'w', zipfile.ZIP_DEFLATED)  # Espera o parâmetro zipfile.ZIP_DEFLATED
