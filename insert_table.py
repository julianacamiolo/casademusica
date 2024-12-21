import sqlite3

conexion = sqlite3.connect("inventario.db")
cursor = conexion.cursor()

# SQL - INSERT INTO nombre_tabla (campos) VALUES (valores)

query = '''
    INSERT INTO productos (nombre, descripcion,categoria,precio)
    VALUES (?, ?, ?, ?)
'''
params = ("Guitarra", "instrumento melodico", "Cuerdas","150.000")
cursor.execute(query,params)
conexion.commit()
print("Instrumento guardado exitosamente")