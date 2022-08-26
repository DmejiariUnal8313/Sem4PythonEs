#programa 3.5: programa03_05.py
#programa para solucionar el problema de verificación de simbolos balanceados
from programa03_01 import Pila #Importar clase Pila el módulo programa03_01

def verificarSimbolos(cadenaSimbolos):
    p = Pila()
    balanceados = True
    indice = 0

    while indice < len(cadenaSimbolos) and balanceados:
        simbolo = cadenaSimbolos[indice]
        if simbolo in "([{":
            p.incluir(simbolo)
        else:
            if p.estaVacia():
                balanceados = false
            else:    
                tope = p.extraer()
                if not parejas(tope,simbolo):
                       balanceados = False
        indice = indice + 1

    if balanceados and p.estaVacia():
        return True
    else:
        return False

def parejas(simboloApertura , simboloCierre):
    aperturas = "([{"
    cierres = ")]}"
    return aperturas.index(simboloApertura) == cierres.index(simboloCierre)
    
