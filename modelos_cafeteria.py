class Producto:
    def __init__(self, numero, nombre, precio, tipo):
        self.numero = numero
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
        
    def mostrar_detalle(self):
        return "ID: " + str(self.numero) + " | " + self.nombre + " ($" + str(self.precio) + ") - Cat: " + self.tipo

class Bebida(Producto):
    def __init__(self, numero, nombre, precio, tipo, tamano, clima):
        super().__init__(numero, nombre, precio, tipo)
        self.tamano = tamano
        self.clima = clima

class Postre(Producto):
    def __init__(self, numero, nombre, precio, tipo, vegano):
        super().__init__(numero, nombre, precio, tipo)
        self.vegano = vegano