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

# ==========================================
#        FUNCIONES CRUD PRINCIPALES
# ==========================================

def registrar_producto(productos):
    print("\n--- REGISTRAR PRODUCTO ---")
    
    # Validación de Código
    while True:
        codigo = input("Escriba el codigo del producto: ").strip()
        if not codigo:
            print("El código no puede estar vacío.")
            continue
        if any(p['codigo'] == codigo for p in productos):
            print("Ya se ha registrado un producto con este codigo.")
            continue
        break
        
    # Validación de Nombre
    while True:
        nombre = input("Escriba el nombre: ").strip()
        if nombre: break
        print("El nombre no puede estar vacío.")
        
    # Validación de Categoría
    while True:
        categoria = input("Escriba la categoria: ").strip()
        if categoria: break
        print("La categoría no puede estar vacía.")

    # Validación de Cantidad
    while True:
        try:
            cantidad = int(input("Escriba la cantidad: "))
            if cantidad >= 0:
                break
            print("La cantidad debe ser mayor o igual a cero.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

    # Validación de Precio
    while True:
        try:
            precio = float(input("Escriba el precio: "))
            if precio > 0:
                break
            print("El precio debe ser mayor que cero.")
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")

    # Creación y guardado del diccionario
    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "cantidad": cantidad,
        "precio": precio
    }
    productos.append(producto)
    print("Producto registrado correctamente.")