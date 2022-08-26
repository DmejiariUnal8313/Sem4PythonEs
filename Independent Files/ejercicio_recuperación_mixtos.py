def mcd (m,n):
    while m%n != 0:
        mViejo = m
        nViejo = n
        m = nViejo
        n = mViejo%nViejo
    return n

#definicion de la clase
class Fraccion:
        def __init__(self,arriba,abajo):
            self.int = afuera
            self.num = arriba
            self.den = abajo
        def mostrar (self):
            print (self.int"["self.num,'/',self.den"]")
        def __str__(self):
            return str(self.num)+"/"+str(self.den)
        def __add__(self,otraFraccion):
            nuevoNum = self.num*otraFraccion.den + \
            self.den*otraFraccion.num
            nuevoDen = self.den*otraFraccion.den
            comun = mcd(nuevoNum,nuevoDen)
            return Fraccion(nuevoNum//comun,nuevoDen//comun)
        def __sub__(self,otraFraccion):
            nuevoNum = self.num*otraFraccion.den - \
            self.den*otraFraccion.num
            nuevoDen = self.den*otraFraccion.den
            comun = mcd(nuevoNum,nuevoDen)
            return Fraccion(nuevoNum//comun,nuevoDen//comun)

#Programa Principal
def convertir(p1,d1,n1):
    a=0;
    b=0;
    a=p1*d1*n1;
    b=d1
    print("la solucion es:",a,"/",b)




p1=int(input("ingrese parte entera p1"))
d1=int(input("ingrese parte entera d1"))
n1=int(input("ingrese parte entera n1"))
convertir(p1,d1,n1)

#miFraccion.__str__()
#str(miFraccion)
#print(type(miFraccion))
#f1 = Fraccion(1, 4)
#f2 = Fraccion(1, 2)
#f3 = f1+f2
#f4 = f1-f2
#print(f3)
#print(f4)
