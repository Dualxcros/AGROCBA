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

def consultar_productos(productos):
    print("\n=====================================")
    print("         CONSULTAR PRODUCTOS")
    print("=====================================")
    if not productos:
        print("No existen registros.")
        return
    for p in productos:
        print("-------------------------------------")
        print(f"Codigo: {p['codigo']}")
        print(f"Nombre: {p['nombre']}")
        print(f"Categoria: {p['categoria']}")
        print(f"Cantidad: {p['cantidad']}")
        print(f"Precio: ${p['precio']}")

def buscar_producto(productos):
    print("\n=====================================")
    print("           BUSCAR PRODUCTO")
    print("=====================================")
    codigo = input("Ingrese el codigo que desea buscar: ").strip()
    
    for p in productos:
        if p['codigo'] == codigo:
            print("-------------------------------------")
            print(f"Codigo: {p['codigo']}")
            print(f"Nombre: {p['nombre']}")
            print(f"Categoria: {p['categoria']}")
            print(f"Cantidad: {p['cantidad']}")
            print(f"Precio: ${p['precio']}")
            return
    print("Producto no encontrado.")

def actualizar_producto(productos):
    print("\n=====================================")
    print("         ACTUALIZAR PRODUCTO")
    print("=====================================")
    codigo = input("Ingrese el codigo del producto que desea actualizar: ").strip()
    
    for p in productos:
        if p['codigo'] == codigo:
            print("Producto encontrado.")
            
            nuevo_nombre = input(f"Escriba el nuevo nombre ({p['nombre']}) o presione Enter para omitir: ").strip()
            if nuevo_nombre: p['nombre'] = nuevo_nombre
            
            nueva_categoria = input(f"Escriba la nueva categoria ({p['categoria']}) o presione Enter para omitir: ").strip()
            if nueva_categoria: p['categoria'] = nueva_categoria
            
            while True:
                nueva_cantidad_str = input(f"Escriba la nueva cantidad ({p['cantidad']}) o presione Enter para omitir: ").strip()
                if not nueva_cantidad_str:
                    break
                try:
                    nueva_cantidad = int(nueva_cantidad_str)
                    if nueva_cantidad >= 0:
                        p['cantidad'] = nueva_cantidad
                        break
                    print("La cantidad debe ser mayor o igual a cero.")
                except ValueError:
                    print("Por favor, ingrese un número entero válido.")

            while True:
                nuevo_precio_str = input(f"Escriba el nuevo precio ({p['precio']}) o presione Enter para omitir: ").strip()
                if not nuevo_precio_str:
                    break
                try:
                    nuevo_precio = float(nuevo_precio_str)
                    if nuevo_precio > 0:
                        p['precio'] = nuevo_precio
                        break
                    print("El precio debe ser mayor que cero.")
                except ValueError:
                    print("Por favor, ingrese un valor numérico válido.")

            print("Producto actualizado correctamente.")
            return
    print("Producto no encontrado.")
    
def eliminar_producto(productos):
    print("\n=====================================")
    print("          ELIMINAR PRODUCTO")
    print("=====================================")
    codigo = input("Ingrese el codigo del producto que desea eliminar: ").strip()
    
    for i, p in enumerate(productos):
        if p['codigo'] == codigo:
            print(f"Producto encontrado: {p['nombre']}")
            confirmacion = input("¿Desea eliminarlo? si / no: ").strip().lower()
            if confirmacion == 'si':
                productos.pop(i)
                print("Producto eliminado correctamente.")
            else:
                print("Eliminacion cancelada.")
            return
    print("Producto no encontrado.")

def calcular_inventario(productos):
    print("\n=====================================")
    total = sum(p['cantidad'] * p['precio'] for p in productos)
    print(f"El valor total del inventario es de: ${total}")




