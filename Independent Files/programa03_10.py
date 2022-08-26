#Programa 3.10: programa03_10.py
#Programa de evaluación de expresiones en notación sufija
from programa03_01 import Pila # Importar clase Pila del modulo programa

def evaluacionNotacionSufija(expresionSufija):
    pilaOperandos = Pila()
    listaSimbolos = expresionSufija.split()
    for simbolo in listaSimbolos:
        if isfloat(simbolo):
            pilaOperandos.incluir(float(simbolo))
        else:
            operando2 = pilaOperandos.extraer()
            operando1 = pilaOperandos.extraer()
            resultado = hacerAritmetica(simbolo,operando1,operando2)
            pilaOperandos.incluir(resultado)
    return pilaOperandos.extraer()

def hacerAritmetica(operador, operandoIzquierda, operandoDerecha):
    if operador == "*":
        return operandoIzquierda * operandoDerecha
    elif operador == "/":
        return operandoIzquierda / operandoDerecha
    elif operador == "+":
        return operandoIzquierda + operandoDerecha
    else:
        return operandoIzquierda - operandoDerecha

def isfloat(simbolo):
    try:
        float(simbolo)
        return True
    except ValueError:
        return False
