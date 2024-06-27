class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def reducir_stock(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            print(f'Se han vendido {cantidad} unidades de {self.nombre}. Stock restante: {self.stock}')
        else:
            print(f'No hay suficiente stock de {self.nombre}.')


class Cliente:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        self.pedidos = []

    def agregar_pedido(self, pedido):
        self.pedidos.append(pedido)
        print(f'Pedido agregado para el cliente {self.nombre}.')


class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.items = []
        self.total = 0

    def agregar_item(self, producto, cantidad):
        if producto.stock >= cantidad:
            self.items.append((producto, cantidad))
            producto.reducir_stock(cantidad)
            self.total += producto.precio * cantidad
            print(f'{cantidad} unidades de {producto.nombre} agregadas al pedido.')
        else:
            print(f'No se pudo agregar {cantidad} unidades de {producto.nombre} al pedido. Stock insuficiente.')

    def mostrar_pedido(self):
        print(f'Pedido de {self.cliente.nombre}:')
        for producto, cantidad in self.items:
            print(f'{producto.nombre} - {cantidad} unidades - ${producto.precio * cantidad}')
        print(f'Total del pedido: ${self.total}')


producto1 = Producto('Manzana', 0.5, 100)
producto2 = Producto('Naranja', 0.75, 80)
producto3 = Producto('Melon', 0.3, 150)

cliente1 = Cliente('Karen', 'jaelakaren2000@gmail.com')

pedido1 = Pedido(cliente1)

pedido1.agregar_item(producto1, 10)
pedido1.agregar_item(producto2, 5)
pedido1.agregar_item(producto3, 20)

pedido1.mostrar_pedido()

cliente1.agregar_pedido(pedido1)

pedido1.agregar_item(producto1, 50)

pedido1.mostrar_pedido()
