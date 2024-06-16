# AutoSixSigma-DataQA

## Objetivo
El objetivo de este proyecto es calcular el índice de calidad Six Sigma utilizando datos extraídos de bases de datos SQL Server. Las reglas de calidad de datos se definen en un archivo JSON y se aplican a los datos obtenidos.

## ¿Para qué?

El objetivo de este proyecto es automatizar el proceso de cálculo del índice de calidad Six Sigma, algo que anteriormente se hacía manualmente y que no es soportado por herramientas comunes como Great Expectations. Este proyecto proporciona una solución automatizada y eficiente para validar la calidad de los datos, permitiendo a las organizaciones identificar y reducir defectos de manera más efectiva. Con AutoSixSigma-DataQA, se facilita la implementación de un control riguroso de la calidad que incluye el cálculo del Six Sigma, mejorando así la precisión y la confiabilidad de los análisis de datos.

## Estructura del Proyecto
```
six_sigma_project/
│
├── data/
│   └── path_to_rules.json
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
- **data/path_to_rules.json**: Archivo JSON que contiene las configuraciones de conexión a la base de datos y las reglas de calidad de datos.
- **exports/**: Carpeta donde se guardarán los archivos HTML generados con los resultados.
- **venv/**: Carpeta del entorno virtual.
- **auto_six_sigma.py**: Script principal que ejecuta el flujo completo del proyecto: lectura de configuración, obtención de datos, aplicación de reglas y cálculo del índice Six Sigma.
- **README.md**: Documentación del proyecto.
- **requirements.txt**: Dependencias del proyecto.
- **.gitignore**: Archivos y directorios a ser ignorados por Git.
- **.env**: Archivo que contiene las variables de entorno necesarias, como la cadena de conexión a la base de datos.

## Requerimientos
- Python 3.6 o superior
- Pandas
- PyODBC
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
   - `data/path_to_rules.json`
   - `.env`

3. Llena los archivos con el contenido proporcionado. El archivo `.env` debe contener la cadena de conexión a la base de datos, por ejemplo:
   ```
   DB_CONN=Driver={SQL Server};Server=your_server;Database=;Trusted_Connection=yes;
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

## Ejemplo de `path_to_rules.json`
```json
{
    "countries": [
        {
            "country_iso2": "PA",
            "rules": [
                {
                    "id": "1",
                    "type": "type1",
                    "desc": "Descripción de la regla 1",
                    "dbname": "nombre_base_de_datos",
                    "query": "SELECT COUNT(*) FROM tabla_completa",
                    "filter": "WHERE condicion_especifica"
                }
            ]
        }
    ]
}
```

## Licencia
Este proyecto está licenciado bajo los términos de la licencia MIT.
