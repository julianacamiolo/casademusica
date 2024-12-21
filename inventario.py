import sqlite3
import json

# Configuración inicial de la base de datos
def inicializar_base_datos():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            precio REAL NOT NULL,
            categoria TEXT NOT NULL,
            cantidad INTEGER NOT NULL DEFAULT 0  -- Nueva columna cantidad
        )
    ''')
    conexion.commit()
    conexion.close()

# Clase para manejar el inventario
class Inventario:
    def __init__(self):
        inicializar_base_datos()

    def agregar_producto(self, nombre, descripcion, precio, categoria, cantidad=0):
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()
        cursor.execute(''' 
            INSERT INTO productos (nombre, descripcion, precio, categoria, cantidad)
            VALUES (?, ?, ?, ?, ?) 
        ''', (nombre, descripcion, precio, categoria, cantidad))
        conexion.commit()
        conexion.close()
        print(f"Producto '{nombre}' agregado exitosamente.")

    def mostrar_productos(self):
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        conexion.close()
        if not productos:
            print("No hay productos en el inventario.")
        else:
            for producto in productos:
                print(f"ID: {producto[0]} - Nombre: {producto[1]} - Descripción: {producto[2]} - Precio: ${producto[3]} - Categoría: {producto[4]} - Cantidad: {producto[5]}")

    def actualizar_producto(self, id_producto, nueva_cantidad):
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()
        cursor.execute(''' 
            UPDATE productos 
            SET cantidad = ? 
            WHERE id = ? 
        ''', (nueva_cantidad, id_producto))
        if cursor.rowcount == 0:
            print(f"No se encontró un producto con ID {id_producto}.")
        else:
            print(f"Cantidad actualizada para el producto con ID {id_producto}.")
        conexion.commit()
        conexion.close()

    def eliminar_producto(self, id_producto):
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()
        cursor.execute(''' 
            DELETE FROM productos 
            WHERE id = ? 
        ''', (id_producto,))
        if cursor.rowcount == 0:
            print(f"No se encontró un producto con ID {id_producto}.")
        else:
            print(f"Producto con ID {id_producto} eliminado exitosamente.")
        conexion.commit()
        conexion.close()

    def buscar_producto(self, nombre):
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()
        cursor.execute(''' 
            SELECT * FROM productos 
            WHERE nombre LIKE ? 
        ''', (f"%{nombre}%",))
        productos = cursor.fetchall()
        conexion.close()
        if productos:
            for producto in productos:
                print(f"ID: {producto[0]} - Nombre: {producto[1]} - Descripción: {producto[2]} - Precio: ${producto[3]} - Categoría: {producto[4]} - Cantidad: {producto[5]}")
        else:
            print(f"No se encontraron productos que coincidan con '{nombre}'.")

# Función principal
if __name__ == "__main__":
    inventario = Inventario()

    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Actualizar cantidad de productos")
        print("4. Eliminar producto")
        print("5. Buscar productos")
        print("6. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        if opcion == 1:
            nombre = input("Nombre del producto: ")
            descripcion = input("Descripción: ")
            try:
                precio = float(input("Precio: ").replace(",", "."))
            except ValueError:
                print("El precio debe ser un número válido.")
                continue
            categoria = input("Categoría: ")
            try:
                cantidad = int(input("Cantidad: "))
            except ValueError:
                print("La cantidad debe ser un número válido.")
                continue
            inventario.agregar_producto(nombre, descripcion, precio, categoria, cantidad)

        elif opcion == 2:
            inventario.mostrar_productos()

        elif opcion == 3:
            try:
                id_producto = int(input("ID del producto a actualizar: "))
                nueva_cantidad = int(input("Nueva cantidad: "))
            except ValueError:
                print("El ID y la cantidad deben ser valores numéricos.")
                continue
            inventario.actualizar_producto(id_producto, nueva_cantidad)

        elif opcion == 4:
            try:
                id_producto = int(input("ID del producto a eliminar: "))
            except ValueError:
                print("El ID debe ser un valor numérico.")
                continue
            inventario.eliminar_producto(id_producto)

        elif opcion == 5:
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == 6:
            print("Saliendo de la aplicación. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")
