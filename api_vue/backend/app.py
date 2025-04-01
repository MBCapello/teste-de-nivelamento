from flask import Flask, request, jsonify
import csv
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)

CSV_FILE = 'data/Relatorio_cadop.csv'

def normalize_text(text):
    """Normaliza texto removendo acentos e caracteres especiais"""
    if not text:
        return ""  # Evita erro com None
    text = text.lower().strip()
    text = re.sub(r'\s+', ' ', text)  # Remove múltiplos espaços
    text = re.sub(r'[áàãâä]', 'a', text)
    text = re.sub(r'[éèêë]', 'e', text)
    text = re.sub(r'[íìîï]', 'i', text)
    text = re.sub(r'[óòôõö]', 'o', text)
    text = re.sub(r'[úùûü]', 'u', text)
    text = re.sub(r'[ç]', 'c', text)
    text = re.sub(r'[^\w\s]', '', text)  # Remove caracteres especiais
    return text

def load_data():
    """Carrega o CSV, tratando erros e removendo linhas inválidas"""
    data = []
    try:
        with open(CSV_FILE, newline='', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file, delimiter=';', quotechar='"')
            for row in reader:
                if not row:  
                    continue  # Ignora linha vazia
                
                # Garante que todos os valores sejam strings válidas
                normalized_row = {k.strip().lower(): (v.strip() if v else '') for k, v in row.items() if k}
                
                if any(normalized_row.values()):  # Garante que a linha não é totalmente vazia
                    data.append(normalized_row)

        if data:
            print(f"📊 {len(data)} registros carregados.")
            print(f"🔍 Exemplo de dados carregados: {data[:2]}")  # Mostra os 2 primeiros registros
        else:
            print("⚠️ CSV lido, mas nenhum dado válido encontrado.")

        return data
    except Exception as e:
        print(f"❌ Erro ao carregar CSV: {e}")
        return []

@app.route('/search', methods=['GET'])
def search():
    """Busca operadoras pelo nome fantasia"""
    query = request.args.get('query', '').strip()
    
    if not query:
        return jsonify({"error": "Query não fornecida"}), 400

    operadoras = load_data()
    
    if not operadoras:
        return jsonify({"error": "Dados não carregados"}), 500

    # Identifica a coluna "Nome Fantasia"
    key_nome_fantasia = next((key for key in operadoras[0].keys() if "nome" in key and "fantasia" in key), None)
    
    if not key_nome_fantasia:
        return jsonify({"error": "Campo Nome Fantasia não encontrado"}), 500

    print(f"🔍 Buscando por: {query}")

    query_normalizada = normalize_text(query)
    resultados = []

    for op in operadoras:
        nome_fantasia = op.get(key_nome_fantasia, "").strip()
        
        if nome_fantasia:
            nome_normalizado = normalize_text(nome_fantasia)

            if query_normalizada in nome_normalizado:
                resultados.append(op)

    if not resultados:
        print(f"❌ Nenhum resultado encontrado para '{query}'.")
        print(f"🔍 Exemplos de nomes no CSV: {[op[key_nome_fantasia] for op in operadoras[:5]]}")

    print(f"✅ {len(resultados)} resultados encontrados para '{query}'")

    return jsonify(resultados)

if __name__ == '__main__':
    app.run(debug=True)
