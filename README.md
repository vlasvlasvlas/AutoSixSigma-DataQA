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
├── auto_six_sigma.py
├── README.md
├── requirements.txt
└── .gitignore
```

### Descripción de Archivos
- **data/path_to_rules.json**: Archivo JSON que contiene las configuraciones de conexión a la base de datos y las reglas de calidad de datos.
- **auto_six_sigma.py**: Script principal que ejecuta el flujo completo del proyecto: lectura de configuración, obtención de datos, aplicación de reglas y cálculo del índice Six Sigma.
- **README.md**: Documentación del proyecto.
- **requirements.txt**: Dependencias del proyecto.
- **.gitignore**: Archivos y directorios a ser ignorados por Git.

## Requerimientos
- Python 3.6 o superior
- Pandas
- PyODBC

## Instalación y Configuración
1. Clona el repositorio o crea el proyecto:
   ```bash
   mkdir six_sigma_project
   cd six_sigma_project
   mkdir data
   ```

2. Crea los archivos necesarios:
   - `auto_six_sigma.py`
   - `data/path_to_rules.json`

3. Llena los archivos con el contenido proporcionado.

4. Instala las dependencias:
   ```bash
   pip install pandas pyodbc
   ```

## Ejecución
Para ejecutar el proyecto, navega al directorio del proyecto y ejecuta el script principal:
```bash
python auto_six_sigma.py
```

Esto ejecutará el flujo completo del proyecto y calculará el índice Six Sigma basado en los datos obtenidos y las reglas aplicadas.

## Licencia
Este proyecto está licenciado bajo los términos de la licencia MIT.
