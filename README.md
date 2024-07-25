# AutoSixSigma-DataQA

## Objetivo
El objetivo de este proyecto es calcular el índice de calidad Six Sigma utilizando datos extraídos de bases de datos SQL Server y PostgreSQL. Las reglas de calidad de datos se definen en un archivo JSON y se aplican a los datos obtenidos.

## ¿Para qué?

El objetivo de este proyecto es automatizar el proceso de cálculo del índice de calidad Six Sigma, algo que usualmente tiene un proceso manual, y no es soportado hasta el momento por herramientas como Great Expectations.

Este proyecto proporciona una solución automatizada y eficiente para validar la calidad de los datos, permitiendo a las organizaciones identificar y reducir defectos de manera más efectiva. Facilita la implementación de un control de la calidad que incluye el cálculo del Six Sigma, mejorando así la precisión y el seguimiento en la confiabilidad de los datos.

## Estructura del Proyecto
```
six_sigma_project/
│
├── data/
│   ├── path_to_rules_mssql.json
│   └── path_to_rules_pgsql.json
│
├── exports/
│   └── [archivos HTML generados]
│
├── venv/
│   └── [entorno virtual]
│
├── auto_six_sigma.py
├── README.md
├── requirements.txt
├── .gitignore
└── .env
```

### Descripción de Archivos
- **data/path_to_rules_mssql.json**: Archivo JSON que contiene las configuraciones de conexión a la base de datos y las reglas de calidad de datos para MS SQL Server.
- **data/path_to_rules_pgsql.json**: Archivo JSON que contiene las configuraciones de conexión a la base de datos y las reglas de calidad de datos para PostgreSQL.
- **exports/**: Carpeta donde se guardarán los archivos HTML generados con los resultados.
- **venv/**: Carpeta del entorno virtual.
- **auto_six_sigma.py**: Script principal que ejecuta el flujo completo del proyecto: lectura de configuración, obtención de datos, aplicación de reglas y cálculo del índice Six Sigma.
- **README.md**: Documentación del proyecto.
- **requirements.txt**: Dependencias del proyecto.
- **.gitignore**: Archivos y directorios a ser ignorados por Git.
- **.env**: Archivo que contiene las variables de entorno necesarias, como las cadenas de conexión a las bases de datos.

## Requerimientos
- Python 3.6 o superior
- Pandas
- PyODBC
- SQLAlchemy
- Python-dotenv

## Instalación y Configuración
1. Clona el repositorio o crea el proyecto:
   ```bash
   mkdir six_sigma_project
   cd six_sigma_project
   mkdir data
   mkdir exports
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

2. Crea y configura los archivos necesarios:
   - `auto_six_sigma.py`
   - `data/path_to_rules_mssql.json`
   - `data/path_to_rules_pgsql.json`
   - `.env`

3. Llena los archivos con el contenido proporcionado. El archivo `.env` debe contener las cadenas de conexión a las bases de datos, por ejemplo:
   ```
   DB_TYPE="mssql"  # O usa "pgsql" para PostgreSQL
   MSSQL_CONN="DRIVER={ODBC Driver 17 for SQL Server};SERVER=your_server;DATABASE=;UID=your_username;PWD=your_password"
   PG_CONN="postgresql://your_username:your_password@your_host:5432/your_database"
   ```

4. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución
Para ejecutar el proyecto, navega al directorio del proyecto y ejecuta el script principal:
```bash
python auto_six_sigma.py
```

Esto ejecutará el flujo completo del proyecto y calculará el índice Six Sigma basado en los datos obtenidos y las reglas aplicadas. Los resultados se guardarán en archivos HTML en la carpeta `exports`.

## Ejemplo de `path_to_rules_mssql.json`
```json
{
  "countries": [
    {
      "country_iso2": "PA",
      "rules": [
        {
          "id": 1,
          "type": "completitud",
          "desc": "Verificar que grupo_fuente_finan no tenga valores nulos",
          "dbname": "PISGRSTG_PAN",
          "query": "select count(*) from dbo.mef_vw_ejecucion",
          "filter": "where grupo_fuente_finan is null"
        },
        {
          "id": 2,
          "type": "completitud",
          "desc": "Verificar que sectorial_sector no tenga nulos",
          "dbname": "PISGRSTG_PAN",
          "query": "select count(*) from dbo.mef_vw_ejecucion",
          "filter": "where sectorial_sector is null"
        }
      ]
    }
  ]
}
```

## Ejemplo de `path_to_rules_pgsql.json`
```json
{
  "countries": [
    {
      "country_iso2": "PA",
      "rules": [
        {
          "id": 1,
          "type": "completitud",
          "desc": "Verificar que grupo_fuente_finan no tenga valores nulos",
          "dbname": "PISGRSTG_PAN",
          "query": "select count(*) from public.mef_vw_ejecucion",
          "filter": "where grupo_fuente_finan is null"
        },
        {
          "id": 2,
          "type": "completitud",
          "desc": "Verificar que sectorial_sector no tenga nulos",
          "dbname": "PISGRSTG_PAN",
          "query": "select count(*) from public.mef_vw_ejecucion",
          "filter": "where sectorial_sector is null"
        }
      ]
    }
  ]
}
```

## Licencia
Este proyecto está licenciado bajo los términos de la licencia MIT.

Espero que este README actualizado cubra todas las nuevas configuraciones y cambios realizados, con las credenciales ofuscadas. Si necesitas más ajustes o información adicional, házmelo saber.