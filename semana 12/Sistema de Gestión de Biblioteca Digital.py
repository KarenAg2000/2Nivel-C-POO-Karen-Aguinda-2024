class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo} por {self.autor} (Categoría: {self.categoria}, ISBN: {self.isbn})"

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        self.libros_prestados.remove(libro)

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}"

class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}
        self.ids_usuarios = set()

    def añadir_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' añadido.")
        else:
            print(f"El libro con ISBN {libro.isbn} ya existe.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            libro = self.libros.pop(isbn)
            print(f"Libro '{libro.titulo}' eliminado.")
        else:
            print(f"No se encontró un libro con ISBN {isbn}.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"Usuario '{usuario.nombre}' registrado.")
        else:
            print(f"El ID de usuario '{usuario.id_usuario}' ya está en uso.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios.pop(id_usuario)
            self.ids_usuarios.remove(id_usuario)
            print(f"Usuario '{usuario.nombre}' dado de baja.")
        else:
            print(f"No se encontró un usuario con ID {id_usuario}.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[id_usuario]
            libro = self.libros.pop(isbn)
            usuario.prestar_libro(libro)
            print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.devolver_libro(libro)
                    self.libros[libro.isbn] = libro
                    print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")
                    return
            print(f"El usuario '{usuario.nombre}' no tiene el libro con ISBN {isbn}.")
        else:
            print(f"Usuario con ID {id_usuario} no encontrado.")

    def buscar_libros(self, criterio, valor):
        resultados = [libro for libro in self.libros.values()
                      if getattr(libro, criterio, '').lower() == valor.lower()]
        if resultados:
            print("Libros encontrados:")
            for libro in resultados:
                print(libro)
        else:
            print(f"No se encontraron libros con {criterio} '{valor}'.")

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            if usuario.libros_prestados:
                print(f"Libros prestados por {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print(f"{usuario.nombre} no tiene libros prestados.")
        else:
            print(f"Usuario con ID {id_usuario} no encontrado.")


# Ejemplo de uso del sistema de gestión de biblioteca
if __name__ == "__main__":
    biblioteca = Biblioteca()

    libro1 = Libro("La Culpa Es de La Vaca", "Varios Autores", "Fábula", "456789123")
    libro2 = Libro("La Conspiración Umbrella: Resident Evil Vol.1", "S.D. Perry", "Ciencia Ficción", "1112131415")
    libro3 = Libro("El amor en los tiempos del cólera", "Gabriel García Márquez", "Romance", "9789588886152")

    biblioteca.añadir_libro(libro1)
    biblioteca.añadir_libro(libro2)
    biblioteca.añadir_libro(libro3)

    usuario1 = Usuario("Karen Aguinda", "user01")
    usuario2 = Usuario("Amparo Intriago", "user02")

    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    biblioteca.prestar_libro("user01", "456789123")
    biblioteca.prestar_libro("user02", "1112131415")

    biblioteca.listar_libros_prestados("user01")
    biblioteca.listar_libros_prestados("user02")

    biblioteca.devolver_libro("user01", "456789123")
    biblioteca.devolver_libro("user02", "1112131415")

    biblioteca.buscar_libros("titulo", "El amor en los tiempos del cólera")
