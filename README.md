# AgroCBA

## Propósito
AgroCBA es una aplicación de consola desarrollada en Python que permite gestionar
los productos de una unidad productiva agropecuaria. Es la primera versión de un
prototipo monolítico: la interfaz, las reglas de negocio y el manejo temporal de
los datos están integrados en un mismo programa.

## Institución
Proyecto desarrollado en el marco de la Formación Profesional Integral del
Centro de Biotecnología Agropecuaria - CBA (SENA), programa Técnico en
Programación de Software.

## Funcionalidades
- Registrar productos, validando que el código no esté vacío ni duplicado.
- Consultar el listado completo de productos registrados.
- Buscar un producto por su código.
- Actualizar nombre, categoría, cantidad y/o precio de un producto existente.
- Eliminar un producto por código, solicitando confirmación previa.
- Calcular el valor total del inventario (cantidad × precio de cada producto).
- Validar los datos ingresados por el usuario (campos vacíos, cantidades y
  precios inválidos, códigos duplicados).

## Tecnologías
- Python 3 (sin dependencias externas).
- Git para el control de versiones.

## Instrucciones de ejecución
1. Clonar o descargar este repositorio.
2. Ubicarse en la carpeta del proyecto.
3. Ejecutar el programa con:

   ```
   python main.py
   ```
4. Seguir las opciones del menú para registrar, consultar, buscar, actualizar,
   eliminar productos o calcular el valor total del inventario.

## Autor(es)
Luis Gerardo Rico Camelo - Técnico en Programación de Software - CBA.