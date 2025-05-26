from config import *

class Estiba:
    def __init__(self, id, nombre, x, y):
        self.id = id
        self.nombre = nombre
        self.x = float(x)
        self.y = float(y)
        self.ubicacion = (self.x, self.y)
        self.lingadas = []

    def agregar_lingada(self, lingada):
        self.lingadas.append(lingada)

    def __repr__(self):
        return f"Estiba({self.id},{self.nombre}, ({self.x},{self.y}), lingadas={len(self.lingadas)})"
