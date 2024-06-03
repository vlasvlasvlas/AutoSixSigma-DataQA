import json

# Lee la configuración desde el JSON.

def read_config(file_path):
    with open(file_path, 'r') as file:
        config = json.load(file)
    return config['connections']
