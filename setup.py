from setuptools import setup, find_packages

setup(
    name='teste_de_nivelamento',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # Adicione as dependências gerais do projeto aqui
    ],
    extras_require={
        'web_scraping': [
            'requests',
            'beautifulsoup4',
            'tqdm',
            'pytest',
            'pytest-cov',
        ],
        'transformacao_dados': [
            # Adicione as dependências para transformacao_dados aqui
        ],
        'banco_dados': [
            # Adicione as dependências para banco_dados aqui
        ],
        'api_vue': [
            # Adicione as dependências para api_vue aqui
        ],
    },
    entry_points={
        'console_scripts': [
            'web_scraping_download = web_scraping.downloader:pdf_downloader',
            'web_scraping_scraper = web_scraping.scraper:get_pdf_links',
            'web_scraping_integrate = integration.integration:main',
        ],
    },
    test_suite='tests',
    tests_require=['pytest'],
)