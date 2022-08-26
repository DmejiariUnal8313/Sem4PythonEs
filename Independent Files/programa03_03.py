#Programa 3.3: programa03_03.py
#Programa la verificación de paréntesis balanceado
from programa03_01 import Pila #importar clase pila del módulo programa03_01.py

def verificarParentesis(cadenaSimbolos):
    p = Pila()
    balanceados = True
    indice = 0
    while indice < len(cadenaSimbolos) and balanceados:
        simbolo = cadenaSimbolos[indice]
        if simbolo == '(':
            p.incluir(simbolo)
        else:
            if p.estaVacia():
                balanceados = False
            else:
                p.extraer()

        indice = indice + 1

    if balanceados and p.estaVacia():
        return True
    else:
        return False
