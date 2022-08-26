#Programa 3.16: programa03_16.py
#implementación de una cola doble en Python
#asumiendo que el final de la cola doble esta en la posición 0 de la lista
class ColaDoble:
    def __init__(self):
        self.items = []
        
    def estaVacia(self):
        return self.items == []
    
    def agregarFrente(self, item):
        self.items.append(item)
        
    def agregarFinal(self, item):
        self.items.insert(0,item)

    def removerFrente(self):
        return self.items.pop()

    def removerFinal(self):
        return self.items.pop(0)
    
    def tamano (self):
        return len (self.items)
