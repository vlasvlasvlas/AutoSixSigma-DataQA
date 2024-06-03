
# Calcula el índice Six Sigma.

def calculate_six_sigma(df):
    defects = df.sum().sum()
    total_opportunities = df.size
    defect_per_unit = defects / total_opportunities
    sigma_level = 1 - defect_per_unit
    return sigma_level * 6  # multiplicar por 6 para obtener el nivel sigma
