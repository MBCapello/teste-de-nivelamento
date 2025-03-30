import os
from unittest.mock import patch
import requests
from web_scraping.downloader import pdf_downloader

def test_downloader_success(tmp_path):
    """Testa se o downloader baixa um arquivo PDF com sucesso."""
    pdf_url = "http://example.com/arquivo.pdf"
    pdf_content = "Conteúdo do PDF de teste".encode("utf-8")

    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.headers = {"Content-Type": "application/pdf"}
        mock_get.return_value.iter_content.return_value = [pdf_content]

        pdf_downloader([pdf_url], save_path=tmp_path)

        pdf_path = os.path.join(tmp_path, "arquivo.pdf")
        assert os.path.exists(pdf_path)
        with open(pdf_path, "rb") as f:
            assert f.read() == pdf_content

def test_downloader_invalid_content_type(tmp_path, capsys):
    """Testa se o downloader lida com um tipo de conteúdo inválido."""
    pdf_url = "http://example.com/arquivo.txt"

    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.headers = {"Content-Type": "text/plain"}

        pdf_downloader([pdf_url], save_path=tmp_path)
        captured = capsys.readouterr()

        assert "Conteúdo inválido (não é PDF)" in captured.out
        pdf_path = os.path.join(tmp_path, "arquivo.txt")
        assert not os.path.exists(pdf_path)

def test_downloader_http_error(tmp_path, capsys):
    """Testa se o downloader lida com um erro HTTP."""
    pdf_url = "http://example.com/arquivo.pdf"

    with patch("requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.RequestException("Erro HTTP")

        pdf_downloader([pdf_url], save_path=tmp_path)
        captured = capsys.readouterr()

        assert "Erro ao baixar" in captured.out
        pdf_path = os.path.join(tmp_path, "arquivo.pdf")
        assert not os.path.exists(pdf_path)