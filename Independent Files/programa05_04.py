from programa03_01 import Pila
from programa05_02 import ArbolBinario
from programa05_03 import *
from evaluarRecursiva import *

def construirArbolAnalisis(expresionAgrupada):
    listaSimbolos = expresionAgrupada.split()
    pilaPadres = Pila()
    arbolExpresion = ArbolBinario('')
    pilaPadres.incluir(arbolExpresion)
    arbolActual = arbolExpresion
    for i in listaSimbolos:
        if i == '(':
            arbolActual.insertarIzquierdo('')
            pilaPadres.incluir(arbolActual)
            arbolActual = arbolActual.obtenerHijoIzquierdo()
        elif i  not in ['+', '-', '*', '/', ')']:
            arbolActual.asignarValorRaiz(int(i))
            padre = pilaPadres.extraer()
            arbolActual = padre
        elif i in ['+', '-', '*', '/']:
            arbolActual.asignarValorRaiz(i)
            arbolActual.insertarDerecho('')
            pilaPadres.incluir(arbolActual)
            arbolActual = arbolActual.obtenerHijoDerecho()
        elif i == ')':
            arbolActual = pilaPadres.extraer()
        else:
            raise ValueError
    return arbolExpresion
    
miArbolAnalisis = construirArbolAnalisis('( ( 10 + 5 ) * 3 )')
preorden(miArbolAnalisis)
print('preorden')
inorden(miArbolAnalisis)
print('inorden')
postorden(miArbolAnalisis)
print('postorden')
print(miArbolAnalisis)
print(evaluar(miArbolAnalisis))


