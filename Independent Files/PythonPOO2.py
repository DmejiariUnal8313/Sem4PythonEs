#definicion de la clase
class NumeroMixto:
        def __init__(self,arriba,abajo,afuera):
            self.ent = afuera
            self.num = arriba
            self.den = abajo
            
        def mostrar (self):
            print (self.ent,"{",self.num,'/',self.den,"}")
            
        def __str__(self):
            return str(self.ent)+"{"+str(self.num)+"/"+str(self.den)+"}"
        
        def __add__(self,otroMixto):
            nuevoEnt = self.ent + otroMixto.ent
            nuevoNum = self.num*otroMixto.den + \
            self.den*otroMixto.num
            nuevoDen = self.den*otroMixto.den
            return NumeroMixto(nuevoEnt,nuevoNum,nuevoDen)
        
        def __sub__(self,otroMixto):
            nuevoEnt = self.ent - otroMixto.ent
            nuevoNum = self.num*otroMixto.den - \
            self.den*otroMixto.num
            nuevoDen = self.den*otroMixto.den
            return NumeroMixto(nuevoEnt,nuevoNum,nuevoDen)

#Programa Principal

f1 = NumeroMixto(3,2,5)
f2 = NumeroMixto(4,1,5)
f3 = f1+f2
f4 = f1-f2
print(f3)
print(f4)
