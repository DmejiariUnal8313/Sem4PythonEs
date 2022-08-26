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
            self.num = arriba
            self.den = abajo
        def mostrar (self):
            print (self.num,'/',self.den)
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
        def __mul__(self,otraFraccion):
            nuevoNum = self.num*otraFraccion.den * \
            self.den*otraFraccion.num
            nuevoDen = self.den*otraFraccion.den
            comun = mcd(nuevoNum,nuevoDen)
            return Fraccion(nuevoNum//comun,nuevoDen//comun)
        def __truediv__(self,otraFraccion):
            nuevoNum = self.num*otraFraccion.den
            nuevoDen = self.den*otraFraccion.num
            comun = mcd(nuevoNum,nuevoNum)
            return Fraccion (nuevoNum//comun,nuevoDen//comun)
#Programa Principal
miFraccion = Fraccion(3, 5)
print (miFraccion)
print ("Comí", miFraccion, "de la pizza")
miFraccion.__str__()
str(miFraccion)
print(type(miFraccion))
f1 = Fraccion(2, 5)
f2 = Fraccion(1, 5)
f3 = f1+f2
f4 = f1-f2
f5 = f1*f2
f6 = f1/f2
print(f3)
print(f4)
print(f5)
print(f6)

#def convertir(p1,d1,n1):
    #a=0;
    #b=0;
    #c=0;
    #a=p1*d1*n1;
    #b=d1;
    #c=p1;
    #print("la solucion es:",c,"{",a,"/",b,"}")


#p1=int(input("ingrese parte entera p1"))
#d1=int(input("ingrese parte entera d1"))
#n1=int(input("ingrese parte entera n1"))



#convertir(p1,d1,n1)



