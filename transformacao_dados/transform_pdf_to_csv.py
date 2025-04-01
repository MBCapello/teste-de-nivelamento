import csv

# Dicionário de substituições de abreviações (conforme a legenda do rodapé)
SUBSTITUICOES = {
    "OD": "Seg. Odontologia",
    "AMB": "Seg. Ambulatorial"
}

def substituir_abreviacoes(row):
    """Substitui as abreviações nos valores das colunas."""
    return {SUBSTITUICOES.get(k, k): SUBSTITUICOES.get(v, v) for k, v in row.items()}


def transform_data_to_csv(data, csv_path):
    """Transforma os dados extraídos em um arquivo CSV, substituindo abreviações."""
    if not data:
        print("Nenhum dado para salvar.")
        return
    
    # Extrai todos os nomes de colunas únicos dos dados
    fieldnames = [SUBSTITUICOES.get(col, col) for col in data[0].keys()]

    try:
        with open(csv_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                row = substituir_abreviacoes(row)  # Aplica a substituição antes de salvar
                writer.writerow({key: row.get(key, "") for key in fieldnames})
        print(f"Dados salvos em {csv_path}")
    except Exception as e:
        print(f"Erro ao salvar CSV: {e}")
