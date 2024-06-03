# Proyecto Six Sigma

## Objetivo
El objetivo de este proyecto es calcular el índice de calidad Six Sigma utilizando datos extraídos de bases de datos SQL Server. Las reglas de calidad de datos se definen en un archivo JSON y se aplican a los datos obtenidos.

## Estructura del Proyecto
```
six_sigma_project/
│
├── data/
│   └── path_to_rules.json
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   ├── rules.py
│   ├── six_sigma.py
│   └── main.py
│
├── .gitignore
├── README.md
├── requirements.txt
└── setup.py
```

### Descripción de Archivos
- **data/path_to_rules.json**: Archivo JSON que contiene las configuraciones de conexión a la base de datos y las reglas de calidad de datos.

- **src/\_\_init\_\_.py**: Archivo para marcar el directorio como un paquete Python.

- **src/config.py**: Contiene la función `read_config` para leer la configuración desde el archivo JSON.

- **src/database.py**: Contiene la función `fetch_data_from_sql` para conectar a la base de datos SQL Server y obtener los datos.

- **src/rules.py**: Contiene la función `apply_rules` para aplicar las reglas de calidad a los datos.

- **src/six_sigma.py**: Contiene la función `calculate_six_sigma` para calcular el índice Six Sigma basado en los resultados de las reglas aplicadas.

- **src/main.py**: Archivo principal que ejecuta el flujo completo del proyecto: lectura de configuración, obtención de datos, aplicación de reglas y cálculo del índice Six Sigma.

- **.gitignore**: Archivos y directorios a ser ignorados por Git.

- **README.md**: Documentación del proyecto.

- **requirements.txt**: Dependencias del proyecto.

- **setup.py**: Configuración del paquete Python.

## Requerimientos
- Python 3.6 o superior
- Pandas
- PyODBC

## Instalación y Configuración
1. Clona el repositorio o descarga el proyecto.
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd six_sigma_project
   ```

2. Instala las dependencias.
   ```bash
   pip install -r requirements.txt
   ```

3. Asegúrate de que el archivo `path_to_rules.json` en el directorio `data/` esté configurado con las conexiones a las bases de datos y las reglas necesarias.

## Ejecución
Para ejecutar el proyecto, navega al directorio del proyecto y ejecuta el script principal:
```bash
python src/main.py
```

También puedes instalar el paquete y ejecutar el comando:
```bash
pip install .
six_sigma
```

Esto ejecutará el flujo completo del proyecto y calculará el índice Six Sigma basado en los datos obtenidos y las reglas aplicadas.

## Licencia
Este proyecto está licenciado bajo los términos de la licencia MIT.
