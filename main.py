import sys
import os

# Asegura que Python pueda ver los módulos dentro del proyecto
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from controllers.participante_ctrl import (
    crear_participante,
    obtener_participante,
    modificar_participante,
    borrar_participante
)

if __name__ == "__main__":
    print("=== TEST DE PARTICIPANTE ===")

    # 🔹 Crear participante
    # crear_participante('12345678', 'Primera', 'Prueba', 'primera.prueba@ucu.edu.uy') EJEMPLO YA CREADO

    # 🔹 Obtener participante
    participante = obtener_participante('12345678')
    print("📋 Datos:")
    for clave, valor in participante.items():
        print(f"  {clave}: {valor}")

    # 🔹 Modificar participante
    # modificar_participante('12345678', email='primera.prueba@ucu.edu.uy')

    # 🔹 Borrar participante
    # borrar_participante('12345678')
