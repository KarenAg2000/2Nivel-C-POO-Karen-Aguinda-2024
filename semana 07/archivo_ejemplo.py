import os

class Archivo:
    def __init__(self, nombre):
        """
        Constructor: inicializa el objeto Archivo.
        Abre el archivo en modo lectura y almacena el nombre del archivo.

        Args:
            nombre (str): El nombre del archivo a abrir.
        """
        self.nombre = nombre
        if os.path.exists(nombre):
            try:
                self.archivo = open(nombre, 'r')
                print(f"Archivo '{self.nombre}' abierto correctamente.")
            except FileNotFoundError:
                self.archivo = None
                print(f"Error: El archivo '{self.nombre}' no existe.")
        else:
            self.archivo = None
            print(f"Error: El archivo '{self.nombre}' no existe en la ruta especificada.")

    def leer_linea(self):
        """
        Lee una línea del archivo.

        Returns:
            str: La línea leída del archivo.
        """
        if self.archivo:
            return self.archivo.readline()
        else:
            return "No se puede leer del archivo porque no fue abierto."

    def leer_todo(self):
        """
        Lee todo el contenido del archivo.

        Returns:
            str: Todo el contenido del archivo.
        """
        if self.archivo:
            return self.archivo.read()
        else:
            return "No se puede leer del archivo porque no fue abierto."

    def __del__(self):
        """
        Destructor: cierra el archivo cuando el objeto es destruido.
        Este método es llamado automáticamente cuando el objeto es recolectado por el recolector de basura.
        """
        if self.archivo:
            self.archivo.close()
            print(f"Archivo '{self.nombre}' cerrado correctamente.")


def main():
    archivo = Archivo('ejemplo.txt')

    print("Primera línea del archivo:", archivo.leer_linea())

    print("Contenido completo del archivo:", archivo.leer_todo())

if __name__ == "__main__":
    main()
