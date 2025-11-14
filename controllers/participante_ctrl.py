import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db.connection import get_connection

def crear_participante(ci, nombre, apellido, email):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            sqlP = "INSERT INTO participante (ci, nombre, apellido, email) VALUES (%s, %s, %s, %s)"
            cur.execute(sqlP, (ci, nombre, apellido, email))
        conn.commit()  # ✅ guarda los cambios
        print(f"✅ Participante {nombre} {apellido} creado correctamente.")
    except Exception as e:
        print("❌ Error al crear participante:", e)
    finally:
        conn.close()

def obtener_participante(ci):
    conn = get_connection()
    try:
        with conn.cursor(dictionary=True) as cur:
            cur.execute("SELECT * FROM participante WHERE ci = %s", (ci,))
            return cur.fetchone()
    finally:
        conn.close()

def modificar_participante(ci, nombre=None, apellido=None, email=None):
    conn = get_connection()
    try:
        updates = []
        params = []
        if nombre:
            updates.append("nombre = %s"); params.append(nombre)
        if apellido:
            updates.append("apellido = %s"); params.append(apellido)
        if email:
            updates.append("email = %s"); params.append(email)
        if not updates:
            print("⚠️ No se proporcionaron campos para actualizar.")
            return
        params.append(ci)
        sqlP = "UPDATE participante SET " + ", ".join(updates) + " WHERE ci = %s"
        with conn.cursor() as cur:
            cur.execute(sqlP, params)
        conn.commit()  # ✅ guarda cambios
        print(f"✅ Participante {ci} actualizado correctamente.")
    except Exception as e:
        print("❌ Error al modificar participante:", e)
    finally:
        conn.close()

def borrar_participante(ci):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM participante WHERE ci = %s", (ci,))
        conn.commit()  # ✅ guarda cambios
        print(f"🗑️ Participante {ci} eliminado.")
    except Exception as e:
        print("❌ Error al borrar participante:", e)
    finally:
        conn.close()

