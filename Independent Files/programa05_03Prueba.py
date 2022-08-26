from programa05_02 import ArbolBinario
from programa05_03 import *

libro = ArbolBinario('Libro')
libro.insertarIzquierdo('Sección 1.1')
libro.insertarIzquierdo('Capitulo 1')
libro.insertarDerecho('Sección 2.2.2')
libro.insertarDerecho('Sección 2.2')
libro.insertarDerecho('Capitulo 2')
libro.obtenerHijoIzquierdo().insertarDerecho('Sección 1.2.2')
libro.obtenerHijoIzquierdo().insertarDerecho('Sección 1.2')
libro.obtenerHijoIzquierdo().obtenerHijoDerecho().insertarIzquierdo('Sección 1.2.1')
libro.obtenerHijoDerecho().insertarIzquierdo('Sección 2.1')
libro.obtenerHijoDerecho().obtenerHijoDerecho().insertarIzquierdo('Sección 2.2.1')

print('Recorrido en preorden:')
preorden(libro)
print('Recorrido en postorden')
postorden(libro)
print('Recorrido en inorden')
inorden(libro)
