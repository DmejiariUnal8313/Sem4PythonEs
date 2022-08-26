class NumeroMixto:
        def __init__(self,afuera,arriba,abajo):
            self.ent = afuera
            self.num = arriba
            self.den = abajo


        def __str__(self):
            print (self.ent,"{",self.num,'/',self.den,"}")

        def __add__(self,OtroMixto):
            if(self.den==OtroMixto.den):
              entero = self.ent+OtroMixto.ent
              numerador = self.num+OtroMixto.num
              denominador = self.den
            else:
              entero = self.ent+OtroMixto.ent 
              numerador = (self.num*OtroMixto.den)+(self.den*OtroMixto.num)             
              denominador = self.den*OtroMixto.den          
            return NumeroMixto(entero,numerador,denominador)


        def __sub__(self,OtroMixto):
            if(self.den==OtroMixto.den):
              entero = self.ent-OtroMixto.ent
              numerador = self.num-OtroMixto.num
              denominador = self.den
            else:
              entero = self.ent-OtroMixto.ent 
              numerador = (self.num*OtroMixto.den)-(self.den*OtroMixto.num)             
              denominador = self.den*OtroMixto.den
            return NumeroMixto(entero,numerador,denominador)

n1 = NumeroMixto(9,1,7)
n2 = NumeroMixto(5,2,6)
n3 = NumeroMixto.__add__(n1,n2)
n4 = NumeroMixto.__sub__(n1,n2)
NumeroMixto.__str__(n3)
NumeroMixto.__str__(n4)
