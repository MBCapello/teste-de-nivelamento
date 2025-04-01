import csv
from db_connection import connect_to_db

def import_operadoras(csv_file_path):
    """ Importa dados das operadoras a partir de um arquivo CSV """
    connection = connect_to_db()
    if not connection:
        return

    try:
        with connection.cursor() as cursor, open(csv_file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file, delimiter=';')

            # Obtém os nomes das colunas do CSV
            csv_columns = csv_reader.fieldnames
            print(f"Colunas do CSV: {csv_columns}")  # Log para depuração

            # Define a ordem correta das colunas para a inserção
            expected_columns = [
                'Registro_ANS', 'CNPJ', 'Razao_Social', 'Nome_Fantasia', 'Modalidade',
                'Logradouro', 'Numero', 'Complemento', 'Bairro', 'Cidade', 'UF', 'CEP',
                'DDD', 'Telefone', 'Fax', 'Endereco_eletronico', 'Representante',
                'Cargo_Representante', 'Regiao_de_Comercializacao', 'Data_Registro_ANS'
            ]

            # Ajusta a consulta SQL para usar placeholders dinâmicos
            placeholders = ', '.join(['%s'] * len(expected_columns))
            sql = f"""
                INSERT INTO operadoras ({', '.join(expected_columns)})
                VALUES ({placeholders})
            """
            print(f"SQL gerado: {sql}")  # Log para depuração

            for row in csv_reader:
                try:
                    # Extrai os valores na ordem correta e substitui vazios por None
                    values = [row.get(col, '').strip() or None for col in expected_columns]
                    print(f"Valores a serem inseridos: {values}")  # Log para depuração

                    cursor.execute(sql, values)
                except Exception as e:
                    print(f"Erro ao inserir linha {row}: {e}")

            connection.commit()
            print("Importação concluída com sucesso!")
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")
    finally:
        connection.close()