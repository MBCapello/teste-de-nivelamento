from setuptools import setup, find_packages

setup(
    name='teste_de_nivelamento',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests==2.32.3',
        'beautifulsoup4==4.13.3',
        'tqdm==4.67.1',
        'pytest==8.3.5',
        'pytest-cov',
        'pandas==2.2.3',
        'pdfplumber==0.11.6',
        'mysql-connector-python==9.2.0',
        'Flask==3.1.0',
        'python-dotenv==1.1.0',
    ],
    extras_require={
        'web_scraping': [
            'requests==2.32.3',
            'beautifulsoup4==4.13.3',
            'tqdm==4.67.1',
            'pytest==8.3.5',
            'pytest-cov',
        ],
        'transformacao_dados': [
            'pandas==2.2.3',
            'pdfplumber==0.11.6',
        ],
        'banco_dados': [
            'mysql-connector-python==9.2.0',
        ],
        'api_vue': [
            'Flask==3.1.0',
            'python-dotenv==1.1.0',
        ],
    },
    entry_points={
        'console_scripts': [
            'main_web_scraping = web_scraping.main:main',  # Executa web_scraping
            'main_transformacao_dados = transformacao_dados.main:main',  # Executa transformacao_dados
            'main_banco_dados = banco_dados.main:main', # Executa banco_dados
            'main_integrate = integration.integration:main',  # Integra tudo (web scraping + transformação de dados)
        ],
    },
    test_suite='tests',
    tests_require=['pytest'],
)
