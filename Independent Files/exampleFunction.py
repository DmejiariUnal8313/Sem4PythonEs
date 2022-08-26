import math

def raizCuadrada(n):
    raiz = n/2
    for k in range(20):
        raiz = (1/2)*(raiz+(n / raiz))
    return raiz
    
print(raizCuadrada(9))
print(raizCuadrada(4563))
print(raizCuadrada(2))
pri



    
