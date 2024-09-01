import json

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio:.2f}"

class Inventario:
    def __init__(self):
        self.productos = {}

    def añadir_producto(self, producto):
        self.productos[producto.get_id()] = producto

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
        else:
            print(f"Producto con ID {id_producto} no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
        else:
            print(f"Producto con ID {id_producto} no encontrado.")

    def buscar_producto(self, nombre):
        resultados = [producto for producto in self.productos.values() if nombre.lower() in producto.get_nombre().lower()]
        return resultados

    def mostrar_productos(self):
        for producto in self.productos.values():
            print(producto)

    def guardar_inventario(self, archivo):
        with open(archivo, 'w') as f:
            json.dump({k: vars(v) for k, v in self.productos.items()}, f, indent=4)

    def cargar_inventario(self, archivo):
        with open(archivo, 'r') as f:
            datos = json.load(f)
            self.productos = {k: Producto(**v) for k, v in datos.items()}

def menu():
    inventario = Inventario()
    archivo = "inventario.json"

    while True:
        print("\nMenú de Gestión de Inventario:")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("7. Cargar inventario")
        print("8. Salir")

        opción = input("Seleccione una opción: ")

        if opción == '1':
            id = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad del producto: "))
            precio = float(input("Precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)
            print("Producto añadido exitosamente.")

        elif opción == '2':
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)
            print("Producto eliminado si existía.")

        elif opción == '3':
            id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco si no se actualiza): ")
            precio = input("Nuevo precio (dejar en blanco si no se actualiza): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)
            print("Producto actualizado si existía.")

        elif opción == '4':
            nombre = input("Nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            for producto in resultados:
                print(producto)
            if not resultados:
                print("No se encontraron productos.")

        elif opción == '5':
            inventario.mostrar_productos()

        elif opción == '6':
            inventario.guardar_inventario(archivo)
            print("Inventario guardado exitosamente.")

        elif opción == '7':
            inventario.cargar_inventario(archivo)
            print("Inventario cargado exitosamente.")

        elif opción == '8':
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
