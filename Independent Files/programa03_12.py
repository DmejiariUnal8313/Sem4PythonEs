from programa03_11 import Cola
from random import randint
def papaCaliente(listaNombre):
    colaSimulacion = Cola()
    for nombre in listaNombre:
        colaSimulacion.agregar(nombre)

    while colaSimulacion.tamano() > 1:
        for i in range(randint(0,10)):
            colaSimulacion.agregar(colaSimulacion.avanzar())

        colaSimulacion.avanzar()

    return colaSimulacion.avanzar()

jugadores = ["Bill","David","Susan","Jane","kent","Brad"]
print(papaCaliente(jugadores))
