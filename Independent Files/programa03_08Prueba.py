#Prueba del programa 3.8: programa03_08Prueba.py
#prueba del programa de conversión de decimal a cualquier base(maximo 16)
from programa03_08 import convertirBase

numeroDecimal = 4579

cadenaOctal = convertirBase(numeroDecimal, 8)
cadenaDoce = convertirBase(numeroDecimal, 12)
cadenaHexadecimal = convertirBase(numeroDecimal, 16)
print("El numero", numeroDecimal, "en octal es", cadenaOctal, \
      "y en hexadecimal es", cadenaHexadecimal)
print("El numero", numeroDecimal, "en base doce es", cadenaDoce)
