import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db.connection import get_connection

def salas_mas_reservadas():
    conn = get_connection()
    try:
        with conn.cursor(dictionary=True) as cur:
            cur.execute("""
                SELECT 
                    r.nombre_sala, 
                    COUNT(rp.id_reserva) AS total_reservas
                FROM reserva r
                JOIN reserva_participante rp ON r.id_reserva = rp.id_reserva
                GROUP BY r.nombre_sala
                ORDER BY total_reservas DESC
                LIMIT 10;
            """)
            return cur.fetchall()
    finally:
        conn.close()

def turnos_mas_demandados():
    conn = get_connection()
    try:
        with conn.cursor(dictionary=True) as cur:
            cur.execute("""
                SELECT 
                    t.id_turno, 
                    t.hora_inicio, 
                    t.hora_fin, 
                    COUNT(r.id_reserva) AS total_reservas
                FROM reserva r
                JOIN turno t ON r.id_turno = t.id_turno
                GROUP BY t.id_turno
                ORDER BY total_reservas DESC;
            """)
            return cur.fetchall()
    finally:
        conn.close()
        
def promedio_participantes_por_sala():
    conn = get_connection()
    try:
        with conn.cursor(dictionary=True) as cur:
            cur.execute("""
                SELECT 
                    r.nombre_sala, 
                    COUNT(rp.ci_participante)/COUNT(DISTINCT r.id_reserva) AS promedio_participantes
                FROM reserva r
                JOIN reserva_participante rp ON r.id_reserva = rp.id_reserva
                GROUP BY r.nombre_sala;
            """)
            return cur.fetchall()
    finally:
        conn.close()