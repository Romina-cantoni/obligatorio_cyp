import sys
import os

def mostrar_resultados(resultados):
    if resultados is None:
        print("No hay datos.")
        return

    if isinstance(resultados, list):
        if len(resultados) == 0:
            print("No hay resultados.")
            return

        if all(isinstance(item, dict) for item in resultados):
            for i, item in enumerate(resultados, 1):
                print(f"\n--- Resultado {i} ---")
                for clave, valor in item.items():
                    print(f"{clave}: {valor}")
            return

        print("\n".join(str(r) for r in resultados))
        return

    if isinstance(resultados, dict):
        if not resultados:
            print("No hay datos.")
            return
        for clave, valor in resultados.items():
            print(f"{clave}: {valor}")
        return

    print(resultados)

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# -------------------------------------------------------------
#                 Importar CONTROLLERS
# -------------------------------------------------------------
from controllers.participante_ctrl import (
    crear_participante,
    obtener_participante,
    modificar_participante,
    borrar_participante
)

from controllers.salas_ctrl import (
    crear_sala,
    obtener_sala,
    modificar_sala,
    borrar_sala
)
# ----------------------------------------------------------
#                       Importar reportes
# ----------------------------------------------------------
from controllers import reportes_ctrl as reportes

# -------------------------------------------------------------
#                       CREACION DE MENUS 
# -------------------------------------------------------------
# --------------------- ABM PARTICIPANTES ---------------------

def menu_participantes():
    while True:
        print("\n--- ABM Participantes ---")
        print("1. Crear participante")
        print("2. Obtener participante")
        print("3. Modificar participante")
        print("4. Borrar participante")
        print("0. Volver")
        opcion = input("Opción: ").strip()
        
        
        if opcion == "1":
            ci = input("CI: ")
            if obtener_participante(ci):
                print("❌ Ya existe el participante con CI:", ci)
                break
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            email = input("Email: ")
            crear_participante(ci, nombre, apellido, email)
        elif opcion == "2":
            ci = input("CI: ")
            resultado = obtener_participante(ci)
            print("📋 Datos:")
            for clave, valor in resultado.items():
                print(f"  {clave}: {valor}")
            if not resultado:
                print("No encontrado")
        elif opcion == "3":
            ci = input("CI: ")
            if not obtener_participante(ci):
                print("❌ No existe el participante con CI:", ci)
                break
            nombre = input("Nuevo nombre (Enter para no modificar): ") or None
            apellido = input("Nuevo apellido (Enter para no modificar): ") or None
            email = input("Nuevo email (Enter para no modificar): ") or None
            modificar_participante(ci, nombre, apellido, email)
        elif opcion == "4":
            ci = input("CI: ")
            borrar_participante(ci)
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

# -------------------------- ABM SALAS --------------------------

def menu_salas():
    while True:
        print("\n--- ABM Salas ---")
        print("1. Crear sala")
        print("2. Obtener sala")
        print("3. Modificar sala")
        print("4. Borrar sala")
        print("0. Volver")
        opcion = input("Opción: ").strip()
        
        
        if opcion == "1":
            nombre_sala = input("Nombre de la sala: ")
            edificio = input("Nombre del edificio: ")
            if obtener_sala(nombre_sala, edificio):
                print("❌ Ya existe la sala:", nombre_sala, "del edificio:", edificio)
                break
            capacidad = input("Capacidad: ")
            tipo_sala = input("Tipo de sala: ")
            crear_sala(nombre_sala, edificio, capacidad, tipo_sala)
        elif opcion == "2":
            nombre_sala = input("Nombre de la sala: ")
            edificio = input("Nombre del edificio: ")
            resultado = obtener_sala(nombre_sala, edificio)
            print("📋 Datos:")
            for clave, valor in resultado.items():
                print(f"  {clave}: {valor}")
            if not resultado:
                print("Sala no encontrada")
        elif opcion == "3":
            nombre_sala = input("Nombre de la sala: ")
            edificio = input("Nombre del edificio: ")
            if not obtener_sala(nombre_sala, edificio):
                print("❌ No existe la sala:", nombre_sala, "del edificio:", edificio)
                break
            capacidad = input("Nueva capacidad (Enter para no modificar): ") or None
            tipo_sala = input("Nuevo tipo de sala (Enter para no modificar): ") or None
            modificar_sala(nombre_sala, edificio, capacidad, tipo_sala)
        elif opcion == "4":
            nombre_sala = input("Nombre de la sala: ")
            edificio = input("Nombre del edificio: ")
            borrar_sala(nombre_sala, edificio)
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

            
def menu_reportes():
    opciones = {
        "1": ("Salas más reservadas", reportes.salas_mas_reservadas),
        "2": ("Turnos más demandados", reportes.turnos_mas_demandados),
        "3": ("Promedio de participantes por sala", reportes.promedio_participantes_por_sala),
        "4": ("Reservas por carrera y facultad", reportes.reservas_por_carrera_facultad),
        "5": ("Porcentaje de ocupación por edificio", reportes.porcentaje_ocupacion_por_edificio),
        "6": ("Reservas y asistencias de profesores y alumnos (grado y posgrado)", reportes.reservas_y_asistencias_profes_y_alumnos),
        "7": ("Sanciones para profesores y alumnos (grado y posgrado)", reportes.sanciones_profes_y_alumnos),
        "8": ("Reservas utilizadas vs cancelada / no asistidas", reportes.reservas_utilizadas_vs_canceladas_na),
        "9": ("top5 de profesores con mas reservas", reportes.profesores_con_mas_reservas)
    }
    
    while True:
        print("\n--- Reportes ---")
        for k, v in opciones.items():
            print(f"{k}. {v[0]}")
        print("0. Volver")
        opcion = input("Opción: ").strip()

        if opcion == "0":
            break
        elif opcion in opciones:
            nombre, funcion = opciones[opcion]
            print(f"\n--- {nombre} ---")
            resultados = funcion()
            mostrar_resultados(resultados)
        else:
            print("Opción inválida.")

# ----------------------------------------------------------
#                       Menu principal
# ----------------------------------------------------------

def main():
    while True:
        print("\n=== SISTEMA DE GESTIÓN ===")
        print("1. Participantes (ABM)")
        print("2. Salas (ABM)")
        print("3. Reportes")
        print("0. Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            menu_participantes()
        if opcion == "2":
            menu_salas()
        elif opcion == "3":
            menu_reportes()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
    