#Programa 3.7: programa03_07
#programa de conversión de decimal a binario, y a otras bases
from programa03_01 import Pila #Importar Pila del módulo programa03_01

def dividirPor2(numeroDecimal):
    pilaResiduo = Pila()

    while numeroDecimal > 0:
        residuo = numeroDecimal % 2
        pilaResiduo.incluir(residuo)
        numeroDecimal = numeroDecimal // 2

    cadenaBinaria = ""
    while not pilaResiduo.estaVacia():
        cadenaBinaria = cadenaBinaria + str(pilaResiduo.extraer())

    return cadenaBinaria
