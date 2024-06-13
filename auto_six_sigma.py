import json
import pandas as pd
import pyodbc
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

def read_config(file_path):
    with open(file_path, 'r') as file:
        config = json.load(file)
    return config['countries']

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
    countries = read_config('data/path_to_rules.json')
    results = []

    for country in countries:
        country_iso2 = country['country_iso2']
        rules = country['rules']
        
        for rule in rules:
            # DB
            dbconn_temp = dbconn.replace('DATABASE=;','DATABASE='+rule['dbname']+';')
            query = rule['query']
            filter = rule['filter']

            data_full = fetch_data_from_sql(query, dbconn_temp)
            data_filter = fetch_data_from_sql(query + " " + filter, dbconn_temp)
            
            results.append({
                "country_iso2": country_iso2,
                "id": rule['id'],
                "regla_tipo": rule['type'],
                "description": rule['desc'],
                "query": query,
                "filter": filter,
                "data_full": data_full.iloc[0, 0],
                "data_filter": data_filter.iloc[0, 0]
            })

    results_df = pd.DataFrame(results)

    # use results_df to calculate the sigma level, must pass 2 columns: "data_full" and "data_filter"
    sigma_level = calculate_six_sigma(results_df)

    # Create a new DataFrame with the required information
    execution_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    final_results = pd.DataFrame([{
        "fecha_ejecucion": execution_date,
        "pais": country_iso2,
        "cantidad_reglas_ejecutadas": len(results_df),
        "score_six_sigma_float": sigma_level,
        "score_six_sigma_round": round(sigma_level)
    }])

    # Print both DataFrames
    print(f"Resultados de las reglas aplicadas:")
    print(results_df)
    print(f"Resultados finales del proceso:")
    print(final_results)
