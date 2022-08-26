#Programa 3.18: programa03_18.py
#implementación de una cola doble en Python
#asumiendo que el final de la cola doble esta en la posición 0 de la lista
class ColaDoble:
    def __init__(self):
        self.items = []
        
    def estaVacia(self):
        return self.items == []
    
    def agregar(self, item):
        if agregar(item, "Frente"):
            self.items.append(item)
        else:
            self.items.insert(0,item)

    def remover(self):
        return self.items.pop()

    def inspeccionar(self):
        return self.items[len(self.items)-1]
