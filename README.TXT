# Inventario de Productos con SQLite

Este proyecto es una aplicación de consola para gestionar un inventario de productos, utilizando Python y una base de datos SQLite. Proporciona funciones para agregar, mostrar, actualizar, eliminar y buscar productos en el inventario.

## Características

- **Agregar productos**: Permite agregar productos con detalles como nombre, descripción, precio, categoría y cantidad.
- **Mostrar productos**: Lista todos los productos almacenados en el inventario.
- **Actualizar cantidad**: Modifica la cantidad de un producto específico.
- **Eliminar productos**: Elimina un producto del inventario usando su ID.
- **Buscar productos**: Encuentra productos por nombre, utilizando coincidencias parciales.
- **Persistencia**: Los datos se almacenan en una base de datos SQLite llamada `inventario.db`.

## Requisitos

- Python 3.6 o superior.
- No se requieren librerías externas, solo el módulo estándar `sqlite3`.

## Instalación

1. Clona este repositorio o copia los archivos en tu máquina.
2. Asegúrate de tener Python instalado.
3. Ejecuta el script principal desde la consola.

```bash
python <nombre_del_archivo>.py