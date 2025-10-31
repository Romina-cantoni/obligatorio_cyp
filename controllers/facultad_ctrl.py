import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db.connection import get_connection

def obtener_facultad(nombre):
    """Devuelve las facultades que coincidan con el nombre dado."""
    conexion = get_connection()
    cursor = conexion.cursor(dictionary=True)

    query = "SELECT id_facultad, nombre FROM facultad WHERE nombre = %s"
    cursor.execute(query, (nombre,))
    resultados = cursor.fetchall()

    cursor.close()
    conexion.close()
    return resultados
