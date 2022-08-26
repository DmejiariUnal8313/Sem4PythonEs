#definicion de la clase
import math

def convertir(p1,n1,d1):       
            a=p1,"{",n1,"/",(d1),"}";
            return a

def adicion(p1,n1,d1,p2,n2,d2):
        if(d1==d2):
                entero = p1+p2
                numerador=n1+n2
                denominador=d1
        else:
                
               a=n1*d2
               b=n2*d1
               numerador=a+b
               denominador=d1*d2
               entero = p1+p2
               
        print("La solución es:",entero,"{",numerador,"/",denominador,"}")

def resta(p1,n1,d1,p2,n2,d2):
        if(d1==d2):
                entero = p1 - p2
                numerador=n1 - n2
                denominador=d1
        else:  
               a=num1*d2
               b=num2*d1
               numerador=a+b
               denominador=d1*d2
               entero = p1 - p2
        print("La solución es:",entero,"{",numerador,"/",denominador,"}")
#Programa Principal
n1=2
d1=5
p1=3
n2=1
d2=5
p2=4
num1=convertir(p1,n1,d1)
print(num1)
num2=convertir(p2,n2,d2)
print(num2)

op=(input("Ingrese la operación"))
if op=='+':
 adicion(p1,n1,d1,p2,n2,d2)
else:
 resta(p1,n1,d1,p2,n2,d2)
