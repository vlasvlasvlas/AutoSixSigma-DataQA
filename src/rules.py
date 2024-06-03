import pandas as pd

# Aplica las reglas de calidad a los datos.

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
