import os
import pymysql
import 

def create_schema():
    """Cria o banco de dados e as tabelas a partir de um arquivo SQL."""
        # Conexão inicial SEM banco (somente para criar o banco)
    temp_connection = pymysql.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            autocommit=True
        )
    temp_cursor = temp_connection.cursor()

    # Criar banco de dados
    temp_cursor.execute("CREATE DATABASE IF NOT EXISTS ans_operadoras;")
    temp_cursor.close()
    temp_connection.close()