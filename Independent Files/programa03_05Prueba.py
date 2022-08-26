#Prueba del programa 3.5: programa03_05Prueba.py
#Prueba del programa para solucionar el problema de
#verificación de símbolos balanceados
from programa03_05 import verificarSimbolos

verificacion = verificarSimbolos("{{([][])}()}")
if verificacion:
    print("Los símbolos están balanceados")
else:
    print("Los símbolos no están balanceados")
