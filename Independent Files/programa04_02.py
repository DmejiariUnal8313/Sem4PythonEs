#programa 4.02: programa04_02.py
#Verión recursiva de la función sumaLista
def sumaLista(numLista):
    
    if len(numLista) == 1: #Caso trivial que permite
        return numLista[0] #salir de la recursión
    else:#Recursión: la función se invoca a si misma
        return numLista[0] + sumaLista(numLista[:])

#Llamado a la función
print(sumaLista([1,3,5,7,9]))
 
