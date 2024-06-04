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

    # sum defects on column "data_filter"
    defects = df['data_filter'].sum()

    print("Defects: ", defects)

    # sum total opportunities on "data_full"
    total_opportunities = df['data_full'].sum()

    print("Total Opportunities: ", total_opportunities)

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
        query = rule['query']
        filter = rule['filter']

        data_full = fetch_data_from_sql(query, dbconn)

        data_filter = fetch_data_from_sql(query+" "+filter, dbconn)
        
        results.append({
            "id": rule['id'],
            "regla_tipo": rule['type'],
            "description": rule['desc'],
            "query": query,
            "filter": filter,
            "data_full": data_full,
            "data_filter": data_filter
        })

    results_df = pd.DataFrame(results)

    # use results_df to calculate the sigma level, must pass 2 columns: "data_full" and "data_filter"
    sigma_level = calculate_six_sigma(results_df)

   

    print(f"Resultados de las reglas aplicadas:")
    print(results_df)
    print(f"El nivel Six Sigma es: {sigma_level}")
