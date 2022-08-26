#Programa 3.11:  programa03_11.py
#Implementación de una cola en python,
#asumiendo que el frente está al final de la lista
class Cola:
    def __init__(self):
        self.items = []
    def estaVacia(self):
        return self.items == []
    def agregar(self, item):
        self.items.insert(0,item)
    def avanzar (self):
        return self.items.pop()
    def tamano (self):
        return len (self.items)
    
