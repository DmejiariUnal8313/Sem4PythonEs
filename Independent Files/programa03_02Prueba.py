#Prueba del Programa 3.2: programa03_02Prueba.py
#Prueba de la implementación de una pila en Python,
#asumiendo que el tope está al principio de la lista

from programa03_02 import Pila
p = Pila()
print(p.estaVacia())
p.incluir(4)
p.incluir('perro')
print(p.inspeccionar())
p.incluir(True)
print(p.tamano())
print(p.estaVacia())
p.incluir(8.4)
print(p.extraer())
print(p.extraer())
print(p.tamano())
