import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db.connection import get_connection

def crear_sala(nombre_sala, edificio, capacidad, tipo_sala):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            sqlS= "INSERT INTO sala (nombre_sala, edificio, capacidad, tipo_sala) VALUES (%s, %s, %s, %s)"
            cur.execute(sqlS, (nombre_sala, edificio, capacidad, tipo_sala))
        conn.commit()  # ✅ guarda los cambios
        print(f"✅ {nombre_sala} en {edificio} creado correctamente.")
    except Exception as e:
        print("❌ Error al crear sala:", e)
    finally:
        conn.close()

def obtener_sala(nombre_sala, edificio):
    conn = get_connection()
    try:
        with conn.cursor(dictionary=True) as cur:
            cur.execute("SELECT * FROM sala WHERE nombre_sala = %s AND edificio = %s", (nombre_sala, edificio))
            return cur.fetchone()
    finally:
        conn.close()

def modificar_sala(nombre_sala, edificio, capacidad=None, tipo_sala=None):
    conn = get_connection()
    try:
        updates = []
        params = []
        if capacidad:
            updates.append("apellido = %s"); params.append(capacidad)
        if tipo_sala:
            updates.append("email = %s"); params.append(tipo_sala)
        if not updates:
            print("⚠️ No se proporcionaron campos para actualizar.")
            return
        params.append(nombre_sala)
        sql1 = "UPDATE sala SET " + ", ".join(updates) + " WHERE nombre_sala = %s"
        params.append(edificio)
        sql2 = "UPDATE sala SET " + ", ".join(updates) + " WHERE edificio = %s"

        with conn.cursor() as cur:
            cur.execute(sql1, params)
            cur.execute(sql2, params)
        conn.commit()  # ✅ guarda cambios
        print(f"✅ Sala {nombre_sala} en {edificio} actualizada correctamente.")
    except Exception as e:
        print("❌ Error al modificar la sala:", e)
    finally:
        conn.close()

def borrar_sala(nombre_sala, edificio):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM sala WHERE nombre_sala = %s AND edificio = %s", (nombre_sala, edificio))
        conn.commit()  # ✅ guarda cambios
        print(f"🗑️ {nombre_sala} en {edificio} eliminada.")
    except Exception as e:
        print("❌ Error al borrar la sala:", e)
    finally:
        conn.close()

