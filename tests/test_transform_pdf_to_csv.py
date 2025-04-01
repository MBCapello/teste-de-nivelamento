from unittest.mock import patch, MagicMock
from transformacao_dados.transform_pdf_to_csv import transform_data_to_csv

def test_transform_data_to_csv():
    """Testa a função transform_data_to_csv."""
    data = [{'PROCEDIMENTO': 'Procedimento 1', 'VIGÊNCIA': '01/01/2025', 'HCO': 'HCO1'}]
    csv_path = 'output.csv'
    
    with patch("csv.DictWriter") as mock_writer:
        # Cria o mock do DictWriter
        mock_csv_writer = MagicMock()
        mock_writer.return_value = mock_csv_writer
        
        # Chama a função de transformação para CSV
        transform_data_to_csv(data, csv_path)

        # Verifica se o método de escrita foi chamado corretamente
        mock_csv_writer.writeheader.assert_called_once()
        mock_csv_writer.writerow.assert_called_once_with({'PROCEDIMENTO': 'Procedimento 1', 'VIGÊNCIA': '01/01/2025', 'HCO': 'HCO1'})
        print("Testando transform_data_to_csv - Teste Completo!")