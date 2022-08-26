#Programa 3.8: programa03_08
#programa de conversión de decimal a cualquier base (maximo 16)
from programa03_01 import Pila #Importar Pila del módulo programa03_01

def convertirBase(numeroDecimal, base):
    digitos = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    pilaResiduo = Pila()

    while numeroDecimal > 0:
        residuo = numeroDecimal % base
        pilaResiduo.incluir(residuo)
        numeroDecimal = numeroDecimal // base

    nuevaCadena = ""
    while not pilaResiduo.estaVacia():
        nuevaCadena = nuevaCadena + digitos[pilaResiduo.extraer()]

    return nuevaCadena
