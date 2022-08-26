#Prueba del programa 3.4: programa03_04Prueba.py
#Prueba del programa para la verificación para la verificación de parentesis
#balanceados
from programa03_04 import verificarParentesis

verificación = verificarParentesis ("(a+b)")
if verificación:
    print("Los paréntesis están balanceados")
else:
    print("Los paréntesis no están balanceados")
