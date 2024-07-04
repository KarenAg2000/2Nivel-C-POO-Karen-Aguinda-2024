class Animal:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser sobrescrito por la clase derivada")

    def __str__(self):
        return f"{self._nombre}, {self._edad} años"


class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self._raza = raza

    def hacer_sonido(self):
        return "Guau!"

    def __str__(self):
        return f"{self._nombre}, {self._edad} años, Raza: {self._raza}"

class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self._color = color

    def hacer_sonido(self):
        return "Miau!"

    def __str__(self):
        return f"{self._nombre}, {self._edad} años, Color: {self._color}"

def main():
    perro = Perro("KAMY", 6, "RUNA")
    gato = Gato("CHISPA", 3, "NEGRO CON BLANCO")

    animales = [perro, gato]

    for animal in animales:
        print(animal)
        print(animal.hacer_sonido())

if __name__ == "__main__":
    main()
