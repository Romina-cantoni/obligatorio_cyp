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
        
def reservas_por_carrera_facultad():
    conn = get_connection()
    try:
        with conn.cursor(dictionary=True) as cur:
            cur.execute("""
                SELECT 
                    f.nombre AS facultad, 
                    pa.nombre_programa AS programa, 
                    COUNT(rp.id_reserva) AS total_reservas
                FROM reserva_participante rp
                JOIN participante_programa_academico ppa ON rp.ci_participante = ppa.ci_participante
                JOIN programa_academico pa ON ppa.nombre_programa = pa.nombre_programa
                JOIN facultad f ON pa.id_facultad = f.id_facultad
                GROUP BY f.id_facultad, pa.nombre_programa;
            """)
            return cur.fetchall()
    finally:
        conn.close()
        
def porcentaje_ocupacion_por_edificio():
    conn = get_connection()
    try:
        with conn.cursor(dictionary=True) as cur:
            cur.execute("""
                SELECT 
                    s.edificio,
                    SUM(CASE WHEN rp.asistencia = TRUE THEN 1 ELSE 0 END)/SUM(s.capacidad)*100 AS porcentaje_ocupacion
                FROM sala s
                JOIN reserva r ON s.nombre_sala = r.nombre_sala AND s.edificio = r.edificio
                JOIN reserva_participante rp ON r.id_reserva = rp.id_reserva
                GROUP BY s.edificio;
            """)
            return cur.fetchall()
    finally:
        conn.close()
        
        
def reservas_y_asistencias_profes_y_alumnos():
    conn = get_connection()
    try:
        with conn.cursor(dictionary=True) as cur:
            cur.execute("""
                SELECT 
                    ppa.rol, 
                    COUNT(rp.id_reserva) AS total_reservas, 
                    SUM(CASE WHEN rp.asistencia = TRUE THEN 1 ELSE 0 END) AS asistencias
                FROM reserva_participante rp
                JOIN participante_programa_academico ppa ON rp.ci_participante = ppa.ci_participante
                GROUP BY ppa.rol;
            """)
            return cur.fetchall()
    finally:
        conn.close()
        
def sanciones_profes_y_alumnos():
    conn = get_connection()
    try:
        with conn.cursor(dictionary=True) as cur:
            cur.execute("""
                SELECT 
                    ppa.rol, 
                    COUNT(sp.ci_participante) AS total_sanciones
                FROM sancion_participante sp
                JOIN participante_programa_academico ppa ON sp.ci_participante = ppa.ci_participante
                GROUP BY ppa.rol;
            """)
            return cur.fetchall()
    finally:
        conn.close()
        
def reservas_utilizadas_vs_canceladas_na():
    conn = get_connection()
    try:
        with conn.cursor(dictionary=True) as cur:
            cur.execute("""
                SELECT
                    SUM(CASE WHEN r.estado = 'finalizada' THEN 1 ELSE 0 END)/COUNT(r.id_reserva)*100 AS porcentaje_utilizadas,
                     SUM(CASE WHEN r.estado IN ('cancelada','sin asistencia') THEN 1 ELSE 0 END)/COUNT(r.id_reserva)*100 AS porcentaje_no_utilizadas
                FROM reserva r;
            """)
            return cur.fetchall()
    finally:
        conn.close()

def profesores_con_mas_reservas():
    conn = get_connection()
    try:
        with conn.cursor(dictionary=True) as cur:
            cur.execute("""
                SELECT 
                    ppa.ci_participante, 
                    COUNT(rp.id_reserva) AS total_reservas
                FROM reserva_participante rp
                JOIN participante_programa_academico ppa ON rp.ci_participante = ppa.ci_participante
                WHERE ppa.rol = 'docente'
                GROUP BY ppa.ci_participante
                ORDER BY total_reservas DESC
                LIMIT 5;
            """)
            return cur.fetchall()
    finally:
        conn.close()
        
        
        