import random

from programa03_11 import Cola
from programa03_13 import Impresora
from programa03_14 import Tarea

def simulacion(numeroSegundos, paginasPorMinuto):

    impresoraLaboratorio = Impresora(paginasPorMinuto)
    colaImpresion = Cola()
    tiemposEspera = []

    for segundoActual in range(numeroSegundos):

        if nuevaTareaImpresion():
            tarea = Tarea(segundoActual)
            colaImpresion.agregar(tarea)

        if (not impresoraLaboratorio.ocupada()) and \
                   (not colaImpresion.estaVacia()):
            tareaSiguiente = colaImpresion.avanzar()
            tiemposEspera.append(tareaSiguiente.tiempoEspera(segundoActual))
            ImpresoraLaboratorio.iniciarNueva(tareaSiguiente)

        impresoraLaboratorio.tictac()
        esperaPromedio=sum(tiemposEspera)/float(len(tiemposEspera))
        print("Tiempo de espera %6.2f segundos %3d tareas restantes." %(esperaPromedio, colaImpresion.tamano()))

def nuevaTareaImpresion():
    numero = random.randrange(1,181)
    if numero == 180:
        return True
    else:
        return False

for i in range(10):
    simulacion(3600,5)
