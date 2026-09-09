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
    codigo = str(input("Ingrese el codigo que desea buscar: ")).strip()
    
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
# ==========================================
#     FUNCIONES DE LOS RETOS ADICIONALES
# ==========================================

def mostrar_total_unidades(productos):
    total = sum(p["cantidad"] for p in productos)
    print(f"\n=> La cantidad total de unidades en el inventario es: {total}")

def producto_mayor_precio(productos):
    if not productos:
        print("\nNo hay productos registrados.")
        return
    mayor = max(productos, key=lambda p: p["precio"])
    print(f"\n=> Producto más caro: {mayor['nombre']} con un precio de ${mayor['precio']}")

def producto_mayor_cantidad(productos):
    if not productos:
        print("\nNo hay productos registrados.")
        return
    mayor = max(productos, key=lambda p: p["cantidad"])
    print(f"\n=> Producto con más stock: {mayor['nombre']} con {mayor['cantidad']} unidades")

def consultar_por_categoria(productos):
    categoria_buscar = input("\nIngrese la categoría que desea buscar: ").strip().lower()
    encontrados = [p for p in productos if p["categoria"].lower() == categoria_buscar]
    
    if encontrados:
        print(f"\n--- PRODUCTOS DE LA CATEGORÍA: {categoria_buscar.upper()} ---")
        for p in encontrados:
            print(f"- {p['nombre']} (Código: {p['codigo']} | Stock: {p['cantidad']})")
    else:
        print("\nNo se encontraron productos en esa categoría.")

def ordenar_alfabeticamente(productos):
    if not productos:
        print("\nNo hay productos registrados.")
        return
    ordenados = sorted(productos, key=lambda p: p["nombre"].lower())
    
    print("\n--- PRODUCTOS ORDENADOS ALFABÉTICAMENTE ---")
    for p in ordenados:
        print(f"- {p['nombre']} | Categoría: {p['categoria']} | Código: {p['codigo']}")
        

def bajo_inventario(productos):
    bajos = [p for p in productos if p["cantidad"] <= 5]
    if bajos:
        print("\n--- ALERTA: PRODUCTOS CON BAJO INVENTARIO ---")
        for p in bajos:
            print(f"- {p['nombre']} (Stock actual: {p['cantidad']})")
    else:
        print("\nTodos los productos tienen un stock saludable (mayor a 5).")

def menu_reportes(productos):
    while True:
        print("\n=====================================")
        print("       REPORTES ADICIONALES           ")
        print("=====================================")
        print("1. Mostrar cantidad total de unidades")
        print("2. Ver producto de mayor precio")
        print("3. Ver producto con mayor stock")
        print("4. Consultar por categoría")
        print("5. Ver productos en orden alfabético")
        print("6. Ver alerta de bajo inventario")
        print("7. Volver al menú principal")
        print("=======================================")
        
        opcion = input("\nSeleccione una opcion: ").strip()
        
        if opcion == "1":
            mostrar_total_unidades(productos)
        elif opcion == "2":
            producto_mayor_precio(productos)
        elif opcion == "3":
            producto_mayor_cantidad(productos)
        elif opcion == "4":
            consultar_por_categoria(productos)
        elif opcion == "5":
            ordenar_alfabeticamente(productos)
        elif opcion == "6":
            bajo_inventario(productos)
        elif opcion == "7":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")


# ==========================================
#         MENÚ PRINCIPAL Y MAIN
# ==========================================

def mostrar_menu():
    print("\n=====================================")
    print("           SISTEMA AGROCBA")
    print("=====================================")
    print("=   1. Registrar producto             =")
    print("=   2. Consultar productos            =")
    print("=   3. Buscar producto                =")
    print("=   4. Actualizar producto            =")
    print("=   5. Eliminar producto              =")
    print("=   6. Mostrar valor total inventario =")
    print("=   7. Reportes Adicionales (Retos)   =")
    print("=   8. Salir                          =")
    print("=======================================")

def main():
    print("=====================================")
    print("           SISTEMA AGROCBA")
    print("=====================================")
    print("Sistema iniciado correctamente")
    
    # Se inicializan los datos cargando el JSON
    productos = cargar_datos()

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opcion: ").strip()

        if opcion == '1':
            registrar_producto(productos)
            guardar_datos(productos)
            
        elif opcion == '2':
            consultar_productos(productos)
            
        elif opcion == '3':
            buscar_producto(productos)
            
        elif opcion == '4':
            actualizar_producto(productos)
            guardar_datos(productos)
            
        elif opcion == '5':
            eliminar_producto(productos)
            guardar_datos(productos)
            
        elif opcion == '6':
            calcular_inventario(productos)
            
        elif opcion == '7':
            menu_reportes(productos)
            
        elif opcion == '8':
            print("\nSaliendo del sistema...")
            break
            
        else:
            print("Opcion invalida. Seleccione una opcion del 1 al 8.")

if __name__ == "__main__":
    main()
    
