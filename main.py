import json
import os

ARCHIVO_JSON = 'producto.json'

def cargar_datos():
    """Carga los productos desde el archivo JSON al iniciar el programa."""
    if os.path.exists(ARCHIVO_JSON):
        with open(ARCHIVO_JSON, 'r', encoding='utf-8') as archivo:
            try:
                return json.load(archivo)
            except json.JSONDecodeError:
                return []
    return []

def guardar_datos(productos):
    """Guarda la lista de productos en el archivo JSON."""
    with open(ARCHIVO_JSON, 'w', encoding='utf-8') as archivo:
        json.dump(productos, archivo, indent=4, ensure_ascii=False)

