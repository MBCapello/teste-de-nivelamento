# Web Scraping para Download de Anexos do Gov.br

Este projeto Python realiza web scraping no site [https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos](https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos) para baixar os Anexos I e II em formato PDF e compactá-los em um arquivo ZIP.

## Funcionalidades

* Extrai os links para os arquivos PDF dos Anexos I e II do site especificado.
* Baixa os arquivos PDF e os salva em um diretório local.
* Compacta todos os arquivos PDF baixados em um único arquivo ZIP.

## Pré-requisitos

* Python 3.6 ou superior
* Bibliotecas Python instaladas (ver seção Instalação)

## Instalação

1.  Clone este repositório:

    ```bash
    git clone git@github.com:MBCapello/teste-de-nivelamento.git
    ```

2.  Navegue até o diretório do projeto:

    ```bash
    cd web_scraping/
    ```

3.  Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

Para executar o script, utilize o seguinte comando:

```bash
python main.py