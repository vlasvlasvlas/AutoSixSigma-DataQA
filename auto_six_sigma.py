import json
import pandas as pd
import pyodbc

def read_config(file_path):
    with open(file_path, 'r') as file:
        config = json.load(file)
    return config['connections']

def fetch_data_from_sql(query, dbconn):
    conn = pyodbc.connect(dbconn)
    data = pd.read_sql(query, conn)
    conn.close()
    return data

def apply_rules(data, rules):
    results = []
    for rule in rules:
        column = rule['data_column']
        if rule['regla_tipo'] == 'completitud':
            rule_result = data[column].notnull()
        elif rule['regla_tipo'] == 'rango':
            condition = rule['condition']
            rule_result = eval(f"data[column].apply(lambda x: {condition})")
        results.append(rule_result.rename(rule['description']))
    return pd.concat(results, axis=1)

def calculate_six_sigma(df):
    defects = df.sum().sum()
    total_opportunities = df.size
    defect_per_unit = defects / total_opportunities
    sigma_level = 1 - defect_per_unit
    return sigma_level * 6  # multiplicar por 6 para obtener el nivel sigma

if __name__ == "__main__":
    connections = read_config('data/path_to_rules.json')

    for conn in connections:
        dbconn = conn['dbconn']
        query = conn['query']
        rules = conn['rules']

        data = fetch_data_from_sql(query, dbconn)
        results_df = apply_rules(data, rules)
        sigma_level = calculate_six_sigma(results_df)

        print(f"Resultados para la conexión {dbconn}:")
        print(results_df)
        print(f"El nivel Six Sigma es: {sigma_level}")
