import pymysql
from banco_dados.db_connection import connect_to_db

def top_10_despesas():
    """Executa as queries SQL para responder à pergunta 3.5, corrigindo o cálculo do último trimestre."""

    connection = connect_to_db()
    if not connection:
        return

    try:
        cursor = connection.cursor()

        # Verificação da existência de dados
        cursor.execute("SELECT COUNT(*) FROM demonstracoes_contabeis")
        count_demonstracoes = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM operadoras")
        count_operadoras = cursor.fetchone()[0]

        if count_demonstracoes == 0 or count_operadoras == 0:
            print("As tabelas demonstracoes_contabeis ou operadoras estão vazias.")
            return

        # Encontra a data máxima na tabela demonstracoes_contabeis
        cursor.execute("SELECT MAX(DATA) FROM demonstracoes_contabeis")
        data_maxima = cursor.fetchone()[0]

        if data_maxima is None:
            print("Não foi possível encontrar a data máxima nos dados.")
            return

        # Calcula a data do início do último trimestre
        data_inicio_trimestre = data_maxima - pymysql.times.timedelta(days=90)

        # Query para o último trimestre
        query_trimestre = f"""
            SELECT
                o.Nome_Fantasia,
                SUM(d.VL_SALDO_FINAL) AS total_despesas
            FROM
                demonstracoes_contabeis d
            JOIN
                operadoras o ON d.REG_ANS = o.Registro_ANS
            WHERE
                d.DATA >= '{data_inicio_trimestre}'
                AND d.DESCRICAO LIKE '%EVENTOS/SINISTROS%'
            GROUP BY
                o.Nome_Fantasia
            ORDER BY
                total_despesas DESC
            LIMIT 10;
        """

        cursor.execute(query_trimestre)
        resultados_trimestre = cursor.fetchall()

        if resultados_trimestre:
            print("\nAs 10 operadoras com maiores despesas no último trimestre:")
            for operadora, despesas in resultados_trimestre:
                print(f"- {operadora}: R$ {despesas:,.2f}")
        else:
            print("\nNenhum resultado encontrado para o último trimestre.")

        # Query para o último ano
        data_inicio_ano = data_maxima - pymysql.times.timedelta(days=365)
        query_ano = f"""
            SELECT
                o.Nome_Fantasia,
                SUM(d.VL_SALDO_FINAL) AS total_despesas
            FROM
                demonstracoes_contabeis d
            JOIN
                operadoras o ON d.REG_ANS = o.Registro_ANS
            WHERE
                d.DATA >= '{data_inicio_ano}'
                AND d.DESCRICAO LIKE '%EVENTOS/SINISTROS%'
            GROUP BY
                o.Nome_Fantasia
            ORDER BY
                total_despesas DESC
            LIMIT 10;
        """

        cursor.execute(query_ano)
        resultados_ano = cursor.fetchall()

        if resultados_ano:
            print("\nAs 10 operadoras com maiores despesas no último ano:")
            for operadora, despesas in resultados_ano:
                print(f"- {operadora}: R$ {despesas:,.2f}")
        else:
            print("\nNenhum resultado encontrado para o último ano.")

    except pymysql.MySQLError as e:
        print(f"Erro ao executar as queries: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if connection:
            connection.close()

def main():
    top_10_despesas()

if __name__ == "__main__":
    main()