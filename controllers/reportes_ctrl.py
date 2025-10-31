import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db.connection import get_connection

def salas_mas_reservadas():
    conn = get_connection()
    try:
        with conn.cursor(dictionary=True) as cur:
            cur.execute("""
                SELECT r.nombre_sala, COUNT(rp.id_reserva) AS total_reservas
                FROM reserva r
                JOIN reserva_participante rp ON r.id_reserva = rp.id_reserva
                GROUP BY r.nombre_sala
                ORDER BY total_reservas DESC
                LIMIT 10;
            """)
            return cur.fetchall()
    finally:
        conn.close()
