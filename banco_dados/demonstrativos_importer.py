import csv
import os
from db_connection import connect_to_db
from datetime import datetime
import pymysql
import logging  # Para um logging mais estruturado

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def import_demonstrativos(directory_path):
    """ Importa os demonstrativos contábeis a partir de arquivos CSV em um diretório """
    connection = connect_to_db()
    if not connection:
        return

    try:
        csv_file_paths = [os.path.join(directory_path, file) for file in os.listdir(directory_path) if file.lower().endswith('.csv')]

        if not csv_file_paths:
            logging.warning(f"Nenhum arquivo CSV encontrado em {directory_path}")
            return

        for csv_file_path in csv_file_paths:
            try:
                cursor = connection.cursor()
                with open(csv_file_path, mode='r', encoding='utf-8') as file:
                    csv_reader = csv.DictReader(file, delimiter=';')

                    expected_columns = ['DATA', 'REG_ANS', 'CD_CONTA_CONTABIL', 'DESCRICAO', 'VL_SALDO_INICIAL', 'VL_SALDO_FINAL']
                    placeholders = ', '.join(['%s'] * len(expected_columns))
                    sql = f"""
                        INSERT INTO demonstracoes_contabeis ({', '.join(expected_columns)})
                        VALUES ({placeholders})
                    """

                    rows_to_insert = []
                    for row in csv_reader:
                        try:
                            values = []
                            for col in expected_columns:
                                value = row.get(col)
                                if value is not None:
                                    value = value.strip()
                                if col == 'DATA':
                                    try:
                                        values.append(datetime.strptime(value, '%Y-%m-%d').strftime('%Y-%m-%d') if value else None)
                                    except ValueError:
                                        try:
                                            values.append(datetime.strptime(value, '%d/%m/%Y').strftime('%Y-%m-%d') if value else None)
                                        except ValueError:
                                            values.append(None)
                                elif col in ['VL_SALDO_INICIAL', 'VL_SALDO_FINAL']:
                                    values.append(float(value.replace(',', '.')) if value else None)
                                else:
                                    values.append(value)
                            rows_to_insert.append(tuple(values))

                        except Exception as row_error:
                            logging.error(f"Erro ao processar linha {row}: {row_error}")

                    try:
                        cursor.executemany(sql, rows_to_insert)
                        logging.info(f"Importação concluída para o arquivo: {csv_file_path}")
                    except pymysql.MySQLError as insert_error:
                        logging.error(f"Erro ao inserir dados: {insert_error}", exc_info=True)

            except Exception as file_error:
                logging.error(f"Erro ao processar o arquivo {csv_file_path}: {file_error}", exc_info=True)

            finally:
                if cursor:
                    cursor.close()

    except Exception as e:
        logging.error(f"Erro ao acessar diretório ou erro geral: {e}", exc_info=True)

    finally:
        if connection:
            connection.close()

def main():
    import_demonstrativos('teste_de_nivelamento/banco_dados/data/demonstrativos/')

if __name__ == "__main__":
    main()