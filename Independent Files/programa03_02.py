#Programa 3.2: programa03_02.py
#implementación alternativa de una pila en Python.
#asumiendo que el tope esta al principio de la lista
#Nota: comparar con la implementación en en el programa 3.1
class Pila:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def incluir(self, items):
        self.items.insert(0,items)

    def extraer(self):
        return self.items.pop(0)

    def inspeccionar(self):
        return self.items[0]

    def tamano(self):
        return len (self.items)
