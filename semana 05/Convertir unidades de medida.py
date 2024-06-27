"""
Programa para convertir unidades de longitud de metros a otras unidades (kilómetros, hectómetros, decámetros, decímetros,
centímetros, milímetros).
Funcionalidad: Permite ingresar una longitud en metros y obtener la conversión a otras unidades de longitud.
"""

def convertir_unidades(metros):
    """
    Función para convertir una longitud dada en metros a otras unidades de longitud.

    :param metros: Longitud en metros (float)
    :return: Diccionario con las conversiones a kilómetros, hectómetros, decámetros, decímetros, centímetros y milímetros
    """
    kilometros = metros / 1000
    hectometros = metros / 100
    decametros = metros / 10
    decimetros = metros * 0.1
    centimetros = metros * 0.01
    milimetros = metros * 0.001

    return {
        'kilometros': kilometros,
        'hectometros': hectometros,
        'decametros': decametros,
        'decimetros': decimetros,
        'centimetros': centimetros,
        'milimetros': milimetros
    }

def mostrar_conversiones(metros, conversiones):
    """
    Función para mostrar las conversiones de longitud.

    :param metros: Longitud en metros (float)
    :param conversiones: Diccionario con las conversiones a otras unidades
    """
    print(f"Longitud en metros: {metros} m")
    print(f"En kilómetros: {conversiones['kilometros']} km")
    print(f"En hectómetros: {conversiones['hectometros']} hm")
    print(f"En decámetros: {conversiones['decametros']} dam")
    print(f"En decímetros: {conversiones['decimetros']} dm")
    print(f"En centímetros: {conversiones['centimetros']} cm")
    print(f"En milímetros: {conversiones['milimetros']} mm")


if __name__ == "__main__":

    longitud_metros = float(input("Ingrese la longitud en metros: "))

    conversiones = convertir_unidades(longitud_metros)

    mostrar_conversiones(longitud_metros, conversiones)