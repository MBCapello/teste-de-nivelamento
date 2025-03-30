from unittest.mock import patch
from web_scraping.scraper import get_pdf_links
import requests

def test_get_pdf_links():
    """Testa a função get_pdf_links."""
    with patch("web_scraping.scraper.requests.get") as mock_get:
        mock_get.return_value.content = b'<html><a href="/Anexo_I.pdf">Anexo I</a><a href="Anexo_II.pdf">Anexo II</a></html>'
        links = get_pdf_links("https://www.gov.br/")
        assert links == ['https://www.gov.br/Anexo_I.pdf', 'https://www.gov.br/Anexo_II.pdf']

def test_get_pdf_links_no_links():
    """Testa get_pdf_links quando não há links de PDF."""
    with patch("web_scraping.scraper.requests.get") as mock_get:
        mock_get.return_value.content = b'<html></html>'
        links = get_pdf_links("https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos")
        assert links == []

def test_get_pdf_links_request_error():
     """Testa se a função trata erros de requisição."""
     with patch("web_scraping.scraper.requests.get") as mock_get:
         mock_get.side_effect = requests.exceptions.RequestException("Request failed")
         links = get_pdf_links("https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos")
         assert links == []