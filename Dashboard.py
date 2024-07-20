import os

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    print(f"Ruta completa del archivo: {ruta_script_absoluta}")  # Línea de depuración
    if os.path.exists(ruta_script_absoluta):
        try:
            with open(ruta_script_absoluta, 'r') as archivo:
                print(f"\n--- Código de {ruta_script} ---\n")
                print(archivo.read())
        except Exception as e:
            print(f"Ocurrió un error al leer el archivo: {e}")
    else:
        print(f"El archivo '{ruta_script_absoluta}' no se encontró.")

def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'semana 02/tarea 2.py',
        '2': 'semana 04/EjemplosMundoReal_POO.py',
        '3': 'semana 05/Convertir unidades de medida.py',
        '4': 'semana 06/Animal.py',
        '5': 'semana 07/archivo_ejemplo.py',
        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            print(f"Ruta construida para el archivo: {ruta_script}")  # Línea de depuración
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
