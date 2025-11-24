#jp

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db.connection import get_connection

def obtener_login(correo, contraseña):
    conn = get_connection()
    try:
        with conn.cursor(dictionary=True) as cur:
            cur.execute("SELECT * FROM login WHERE correo = %s AND contraseña = %s", (correo, contraseña))
            return cur.fetchone()
    finally:
        conn.close()


def existe_login(correo):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT 1 FROM login WHERE correo = %s", (correo,))
            return cur.fetchone() is not None
    finally:
        conn.close()

def crear_login(correo, contraseña, ci):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO login (correo, contraseña, ci) VALUES (%s, %s, %s)",(correo, contraseña, ci))
            return cur.fetchone()
    finally:
        conn.close()