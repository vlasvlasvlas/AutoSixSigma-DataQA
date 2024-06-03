import json
import pandas as pd
import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

def read_config(file_path):
    with open(file_path, 'r') as file:
        config = json.load(file)
    return config['rules']

def fetch_data_from_sql(query, dbconn):
    conn = pyodbc.connect(dbconn)
    data = pd.read_sql(query, conn)
    conn.close()
    return data

def calculate_six_sigma(df):
    defects = df.sum().sum()
    total_opportunities = df.size
    defect_per_unit = defects / total_opportunities
    sigma_level = 1 - defect_per_unit
    return sigma_level * 6  # multiplicar por 6 para obtener el nivel sigma

if __name__ == "__main__":
    dbconn = os.getenv("DB_CONN")
    rules = read_config('data/path_to_rules.json')
    results = []

    for rule in rules:
        # DB
        dbconn = dbconn.replace('DATABASE=;','DATABASE='+rule['dbname']+';')
        print(dbconn)        
        query = rule['query']
        print(query)
        data = fetch_data_from_sql(query, dbconn)
        print(data)
        
        results.append({
            "id": rule['id'],
            "regla_tipo": rule['regla_tipo'],
            "description": rule['description'],
            "query": query,
            "resultado": data
        })

    results_df = pd.DataFrame(results)
    sigma_level = calculate_six_sigma(results_df[['resultado']])

    print(f"Resultados de las reglas aplicadas:")
    print(results_df)
    print(f"El nivel Six Sigma es: {sigma_level}")
