from unittest.mock import patch, MagicMock
from transformacao_dados.extract_pdf import extract_data

def test_extract_data():
    """Testa a função extract_data para garantir que dados sejam extraídos corretamente."""

    # Caminho do PDF de teste (simulando um arquivo com prefixo "Anexo_I")
    pdf_path = 'Anexo_I_arquivo.pdf'
    
    # Mock de retorno da função extract_tables
    mock_data = [
        ['PROCEDIMENTO', 'VIGÊNCIA', 'HCO'],
        ['Procedimento 1', '01/01/2025', 'HCO1'],
        ['Procedimento 2', '02/02/2025', 'HCO2']
    ]
    
    # Patch do pdfplumber.open para simular o comportamento do PDF
    with patch('pdfplumber.open') as mock_open:
        mock_pdf = MagicMock()
        mock_page = MagicMock()
        mock_pdf.pages = [mock_page]
        
        # Simulando que a função extract_tables retorna os dados mockados
        mock_page.extract_tables.return_value = mock_data
        mock_open.return_value.__enter__.return_value = mock_pdf
        
        # Chamando a função que testa a extração
        data = extract_data(pdf_path)
        
        # Verifique se os dados extraídos são os esperados
        assert len(data) == 3  # Espera-se 3 linhas (contando cabeçalho + 2 dados)
        assert data[0] == ['PROCEDIMENTO', 'VIGÊNCIA', 'HCO']
        assert data[1] == ['Procedimento 1', '01/01/2025', 'HCO1']
        assert data[2] == ['Procedimento 2', '02/02/2025', 'HCO2']
