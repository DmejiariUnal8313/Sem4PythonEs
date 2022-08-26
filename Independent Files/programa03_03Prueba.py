#Prueba del programa 3.3: programa03_03Prueba.py
#Prueba del programa para la verificación para la verificación de parentesis
#balanceados
from programa03_03 import verificarParentesis

verificación = verificarParentesis ("(a+b)")
if verificación:
    print("Los paréntesis están balanceados")
else:
    print("Los paréntesis no están balanceados")
