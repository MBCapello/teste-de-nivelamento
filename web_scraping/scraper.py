import requests
from urllib.parse import urlparse 
from bs4 import BeautifulSoup
  
def get_pdf_links(url):
    """_Extrai os links dos pdf's anexo I e II da URL passada nos parametros_
    """
    try:
        response = requests.get(url)
        response.raise_for_status() #Lança exceção para bad response
        soup = BeautifulSoup(response.content, "html.parse")
        pdf_links = []
        for link in soup.find_all("a", href=True):
            href = link['href']
            if("Anexo_I" in href or "Anexo_II" in href) and href.endwith(".pdf"):
                if not bool(urlparse(href).netloc):
                    href = url.rstrip("/") + "/" + href.lstrip("/") #Converte URLs relativos em absolutos.
                pdf_links.append(href)
        print(f"{len(pdf_links)} pdf's encontrados.")
        return pdf_links
    except requests.exceptions.RequestException as erro:
        print(f"Falha ao acessar o site: {erro}")
        return []
    except Exception as erro:
        print(f"Desculpa, ocorreu um erro, tente mais tarde. {erro}")
        return []
    
if __name__ == '__main__':
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    links = get_pdf_links(url)
    print(links)
    
        
        
