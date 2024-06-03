import pandas as pd
import pyodbc

# Maneja la conexión a la base de datos y la obtención de datos.

def fetch_data_from_sql(query, dbconn):
    conn = pyodbc.connect(dbconn)
    data = pd.read_sql(query, conn)
    conn.close()
    return data
