#Prueba del programa 3.6: programa03_06Prueba.py
#Prueba del programa para solucionar el problema de
#verificación de símbolos y numeros balanceados
from programa03_05 import verificarSimbolos

verificacion = verificarSimbolos("{{([a][b])}()}")
if verificacion:
    print("Los símbolos están balanceados")
else:
    print("Los símbolos no están balanceados")
