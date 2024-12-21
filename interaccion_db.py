import sqlite3


# Configuración inicial de la base de datos

conexion = sqlite3.connect("inventario.db")
cursor = conexion.cursor()

query = '''
    CREATE TABLE IF NOT EXISTS productos (
        id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        precio REAL NOT NULL,
        categoria TEXT NOT NULL,
        cantidad 
    )
'''
cursor.execute(query)
conexion.commit()
conexion.close()




