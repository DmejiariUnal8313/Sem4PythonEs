#Programa 4.03: programa04_03.py
#Conversión de un entero a una cadena en base 2  16
def aCadena(n,base):
    cadenaConversion = "0123456789ABCDEF"
    if n < base:                  #Caso base que permite  
        return cadenaConversion[n]#salir de la recursión
    else:#Recursión y concatenación de residuos (caracteres)
        return aCadena(n//base,base) + cadenaConversion[n%base]
    
# LLamados a la función
print(aCadena(769,16))#Convierte 769 a su cadena en decimal
print(aCadena(769,2)) #convierte 769 a su cadena en binario
