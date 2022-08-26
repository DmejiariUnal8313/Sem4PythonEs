#Programa 3.9: programa03_09.py
#Programa de conversión de notación infija a notación sufija
from programa03_01 import Pila
import string
def infija_a_sufija(expresionInfija):
    precedencia = {}
    precedencia ["*"] = 3
    precedencia ["/"] = 3
    precedencia ["+"] = 2
    precedencia ["-"] = 2
    precedencia ["("] = 1
    pilaOperadores = Pila()
    listaSufija = []
    listaSimbolos = expresionInfija.split()
    for simbolo in listaSimbolos:
        if simbolo in string.ascii_uppercase or simbolo.isdecimal():
            listaSufija.append(simbolo) 
        elif simbolo == "(":
            pilaOperadores.incluir(simbolo)
        elif simbolo == ")":
            simboloTope = pilaOperadores.extraer()
            while simboloTope != "(":
                listaSufija.append(simboloTope)
                simboloTope = pilaOperadores.extraer()
        else:
            while (not pilaOperadores.estaVacia()) and \
                  (precedencia[pilaOperadores.inspeccionar()] >= \
                   precedencia[simbolo]):
                    listaSufija.append(pilaOperadores.extraer())
            pilaOperadores.incluir(simbolo)
    while not pilaOperadores.estaVacia():
        listaSufija.append(pilaOperadores.extraer())
    return " ".join(listaSufija)
