# Análise de Dados da ANS - Projeto de Estágio

### Descrição do Projeto

Este projeto foi desenvolvido como parte de um teste de nivelamento para uma vaga de estágio. O objetivo era criar um sistema que integrasse web scraping, transformação de dados, análise de banco de dados e desenvolvimento de API para extrair e analisar informações relevantes do site da Agência Nacional de Saúde Suplementar (ANS).

### Funcionalidades

1.  **Web Scraping:**
    * Extração dos links para os arquivos PDF dos Anexos I e II do site da ANS.
    * Download dos arquivos PDF.
    * Compactação dos arquivos em um arquivo ZIP.
2.  **Transformação de Dados:**
    * Extração dos dados da tabela "Rol de Procedimentos e Eventos em Saúde" do Anexo I.
    * Conversão dos dados para formato CSV.
    * Substituição das abreviações das colunas "OD" e "AMB" pelas descrições completas.
    * Compactação do CSV em um arquivo ZIP.
3.  **Banco de Dados:**
    * Criação de um banco de dados MySQL para armazenar os dados das operadoras e demonstrações contábeis.
    * Importação dos dados dos arquivos CSV para o banco de dados.
    * Implementação de queries SQL para identificar as 10 operadoras com as maiores despesas em "EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" nos últimos trimestre e ano.
4.  **API com Vue.js:**
    * Desenvolvimento de uma API Flask para realizar buscas textuais nos cadastros das operadoras.
    * Criação de uma interface Vue.js para interagir com a API.
    * Elaboração de uma coleção Postman para demonstrar o funcionamento da API.

### Percalços e Desafios

* **Atraso na Entrega:**
    * A conciliação do teste com outros compromissos resultou em um atraso na entrega.
* **Complexidade dos Dados:**
    * A extração e transformação dos dados dos PDFs exigiram um grande esforço devido à complexidade e inconsistência dos formatos.
* **Integração de Tecnologias:**
    * A integração de Python, SQL e Vue.js demandou um bom conhecimento de cada tecnologia e atenção aos detalhes para garantir a compatibilidade e o bom funcionamento do sistema.
* **Configuração do Banco de Dados:**
    * A configuração do banco de dados MySQL e a importação dos dados exigiram um tempo considerável para garantir a integridade e a correta estruturação das tabelas.
* **Aprendizado do Vue.js:**
    * O desenvolvimento da interface Vue.js foi um desafio, pois exigiu um aprendizado rápido da tecnologia para cumprir os prazos.

### Funcionamento do Projeto

1.  **Instalação:**
    * Certifique-se de ter Python, Node.js e MySQL instalados.
    * Instale as dependências usando o `pip install -e .` (ou `pip install -e .[nome_do_modulo]` para módulos específicos).
2.  **Execução dos Scripts:**
    * `main_web_scraping`: Baixa os arquivos do site da ANS.
    * `main_transformacao_dados`: Transforma os dados dos PDFs em CSVs.
    * `main_banco_dados`: Importa os dados para o banco de dados e realiza as análises.
    * Para a API, execute o servidor Flask e acesse a interface Vue.js no navegador.
3.  **Testes:**
    * Execute os testes com `pytest` e gere o relatório de cobertura com `pytest --cov=nome_do_pacote`.

### Estrutura do Projeto

A estrutura do projeto é definida no arquivo `setup.py`, que utiliza `find_packages()` para encontrar e incluir todos os pacotes Python no projeto. Os scripts executáveis são definidos na seção `entry_points`, que mapeia os scripts para as funções `main` nos respectivos módulos.

├── api_vue
│   ├── init.py
│   ├── app.py
│   └── ...
├── banco_dados
│   ├── init.py
│   ├── db_connection.py
│   ├── demonstrativos_importer.py
│   ├── main.py
│   ├── operadoras_importer.py
│   └── ...
├── integration
│   ├── init.py
│   ├── integration.py
│   └── ...
├── transformacao_dados
│   ├── init.py
│   ├── compact_csv.py
│   ├── extract_pdf.py
│   ├── main.py
│   └── ...
├── web_scraping
│   ├── init.py
│   ├── downloader.py
│   ├── main.py
│   ├── scraper.py
│   └── ...
├── setup.py
└── ...


### Dependências

beautifulsoup4==4.13.3
blinker==1.9.0
certifi==2025.1.31
cffi==1.17.1
chardet==5.2.0
charset-normalizer==3.4.1
click==8.1.8
colorama==0.4.6
cryptography==44.0.2
et_xmlfile==2.0.0
Flask==3.1.0
flask-cors==5.0.1
idna==3.10
iniconfig==2.1.0
itsdangerous==2.2.0
Jinja2==3.1.6
lxml==5.3.1
MarkupSafe==3.0.2
mysql-connector-python==9.2.0
numpy==2.2.4
opencv-python-headless==4.11.0.86
openpyxl==3.1.5
packaging==24.2
pandas==2.2.3
pdfminer.six==20250327
pdfplumber==0.11.6
pillow==11.1.0
pluggy==1.5.0
pycparser==2.22
PyMySQL==1.1.1
pypdf==5.4.0
PyPDF2==3.0.1
pypdfium2==4.30.1
pytest==8.3.5
python-dateutil==2.9.0.post0
python-dotenv==1.1.0
pytz==2025.2
requests==2.32.3
setuptools==78.1.0
six==1.17.0
soupsieve==2.6
tabulate==0.9.0
-e git+ssh://git@github.com/MBCapello/teste-de-nivelamento.git@0a802cbd4139b4ba8531f73e92469b07d3a84276#egg=teste_de_nivelamento
tqdm==4.67.1
typing_extensions==4.13.0
tzdata==2025.2
urllib3==2.3.0
Werkzeug==3.1.3


### Considerações Finais

Apesar dos desafios e do atraso, este projeto demonstra minha capacidade de desenvolver um sistema completo e funcional, integrando diversas tecnologias e lidando com dados complexos. Agradeço a oportunidade de apresentar este trabalho e espero que ele demonstre meu potencial como estagiário.