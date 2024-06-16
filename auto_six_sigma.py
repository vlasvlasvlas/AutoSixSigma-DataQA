import json
import pandas as pd
import pyodbc
import os
from dotenv import load_dotenv
from datetime import datetime
from string import Template

load_dotenv()

EXPORT_FOLDER = "exports"


def read_config(file_path):
    with open(file_path, "r") as file:
        config = json.load(file)
    return config["countries"]


def fetch_data_from_sql(query, dbconn):
    conn = pyodbc.connect(dbconn)
    data = pd.read_sql(query, conn)
    conn.close()
    return data


def calculate_six_sigma(df):
    global defects, total_opportunities, defects_per_million_opportunities

    defects = df["data_filter"].sum()
    print("Defects: ", defects)

    total_opportunities = df["data_full"].sum()
    print("Total Opportunities: ", total_opportunities)

    defects_per_million_opportunities = (defects * 1_000_000) / total_opportunities
    print("DPMO: ", defects_per_million_opportunities)

    if defects_per_million_opportunities > 308537:
        sigma_level = 1
    elif defects_per_million_opportunities > 66807:
        sigma_level = 2
    elif defects_per_million_opportunities > 6210:
        sigma_level = 3
    elif defects_per_million_opportunities > 233:
        sigma_level = 4
    elif defects_per_million_opportunities > 3.4:
        sigma_level = 5
    else:
        sigma_level = 6

    return sigma_level


def export_to_html(df1, df2, country_iso2, execution_date, folder_name):
    file_name = f"{country_iso2}_{execution_date}.html"
    file_path = os.path.join(folder_name, file_name)

    html_template = Template(
        """
    <html>
    <head>
        <title>Six Sigma Report</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
        <style>
            body {
                padding: 20px;
            }
            .table-container {
                margin-bottom: 40px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="table-container">
                <h1>Resultados de las reglas aplicadas</h1>
                $table1
            </div>
            <div class="table-container">
                <h1>Resultados finales del proceso</h1>
                $table2
            </div>
        </div>
    </body>
    </html>
    """
    )

    html_content = html_template.substitute(
        table1=df1.to_html(classes="table table-striped table-bordered", index=False),
        table2=df2.to_html(classes="table table-striped table-bordered", index=False),
    )

    os.makedirs(folder_name, exist_ok=True)

    with open(file_path, "w") as file:
        file.write(html_content)


if __name__ == "__main__":
    dbconn = os.getenv("DB_CONN")
    countries = read_config("data/path_to_rules.json")
    results = []

    for country in countries:
        country_iso2 = country["country_iso2"]
        rules = country["rules"]

        for rule in rules:
            dbconn_temp = dbconn.replace(
                "DATABASE=;", "DATABASE=" + rule["dbname"] + ";"
            )
            query = rule["query"]
            filter = rule["filter"]

            data_full = fetch_data_from_sql(query, dbconn_temp)
            data_filter = fetch_data_from_sql(query + " " + filter, dbconn_temp)

            results.append(
                {
                    "country_iso2": country_iso2,
                    "id": rule["id"],
                    "regla_tipo": rule["type"],
                    "description": rule["desc"],
                    "query": query,
                    "filter": filter,
                    "data_full": data_full.iloc[0, 0],
                    "data_filter": data_filter.iloc[0, 0],
                }
            )

    results_df = pd.DataFrame(results)

    sigma_level = calculate_six_sigma(results_df)

    execution_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    final_results = pd.DataFrame(
        [
            {
                "fecha_ejecucion": execution_date,
                "pais": results_df["country_iso2"].iloc[0],
                "cantidad_reglas_ejecutadas": len(results_df),
                "defects": defects,
                "total_opportunities": total_opportunities,
                "defects_per_million_opportunities": defects_per_million_opportunities,
                "score_six_sigma": sigma_level,
            }
        ]
    )

    print(f"Resultados de las reglas aplicadas:")
    print(results_df)
    print(f"Resultados finales del proceso:")
    print(final_results)

    export_to_html(
        results_df, final_results, country_iso2, execution_date, EXPORT_FOLDER
    )
