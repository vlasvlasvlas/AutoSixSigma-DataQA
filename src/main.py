from src.config import read_config
from src.database import fetch_data_from_sql
from src.rules import apply_rules
from src.six_sigma import calculate_six_sigma

# Ejecuta el flujo completo del proyecto.

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
