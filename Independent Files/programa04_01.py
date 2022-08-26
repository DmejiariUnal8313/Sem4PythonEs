#Programa 4.01: programa04_01.py
#La función de suma iterativa
def sumaLista(numLista):
    laSuma = 0
    for i in numLista:
        laSuma = laSuma + i
    return laSuma

#Llamado a la función
print(sumaLista([1,3,5,7,9]))
