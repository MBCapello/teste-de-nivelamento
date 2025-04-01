import pymysql
from banco_dados.db_connection import connect_to_db
from banco_dados.operadoras_importer import import_operadoras
from banco_dados.demonstrativos_importer import import_demonstrativos
from banco_dados.top_10_despesas import top_10_despesas
from banco_dados.create_schema import create_schema

def main():
    try:
        # Agora, conectar DIRETAMENTE ao banco criado
        connection = create_schema()
        cursor = connection.cursor()

        # Ler o schema.sql e rodar os comandos
        with open('sql/schema.sql', 'r') as file:
            schema_sql = file.read()

        for query in schema_sql.split(";"):
            query = query.strip()
            if query:
                cursor.execute(query)

        print("Banco de dados e tabelas criados com sucesso!")

        return connection, cursor  # Retorna a conexão já configurada

    except pymysql.MySQLError as err:
        print(f"Erro ao criar o banco ou tabelas: {err}")
        return None, None
    except Exception as e:
        print(f"Erro ao ler o arquivo schema.sql: {e}")
        return None, None

def main():
    """Função principal para rodar as importações de CSVs."""
    print("Criando o schema do banco de dados...")
    connection, cursor = connect_to_db()

    if connection is None or cursor is None:
        print("Erro crítico: Banco de dados não pôde ser criado.")
        return  # Sai do programa se não tiver conexão

    try:
        # Caminhos dos arquivos
        operadoras_path = 'data/operadoras/Relatorio_cadop.csv'
        demonstrativos_path = 'data/demonstrativos'

        # Importando os dados
        print("Importando dados das operadoras...")
        import_operadoras(operadoras_path)

        print("Importando dados dos demonstrativos...")
        import_demonstrativos(demonstrativos_path)

        print("Importações realizadas com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro durante a execução do script: {e}")

    finally:
        # Fechar conexões
        top_10_despesas()
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection:
            connection.close()

if __name__ == "__main__":
    main()