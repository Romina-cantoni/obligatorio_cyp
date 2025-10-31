import os
import mysql.connector
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

def get_connection():
    """Crea y devuelve una conexión a la base de datos MySQL."""
    try:
        conexion = mysql.connector.connect(
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_NAME'),
            auth_plugin='mysql_native_password'
        )
        return conexion
    except mysql.connector.Error as err:
        print("❌ Error al conectar a MySQL:", err)
        return None

if __name__ == "__main__":
    conexion = get_connection()
    if conexion:
        print("✅ Conexión exitosa a MySQL")
        conexion.close()
