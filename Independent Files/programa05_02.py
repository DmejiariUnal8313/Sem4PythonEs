#definición de clase ArbolBinario



class ArbolBinario:
    def __init__(self,objetoRaiz):
        self.clave = objetoRaiz
        self.hijoIzquierdo = None
        self.hijoDerecho = None

    def insertarIzquierdo(self, nuevoNodo):
        if self.hijoIzquierdo == None:
            self.hijoIzquierdo = ArbolBinario(nuevoNodo)
        else:
            t = ArbolBinario(nuevoNodo)
            t.hijoIzquierdo = self.hijoIzquierdo
            self.hijoIzquierdo = t

    def insertarDerecho(self, nuevoNodo):
        if self.hijoDerecho == None:
            self.hijoDerecho = ArbolBinario(nuevoNodo)
        else:
            t = ArbolBinario(nuevoNodo)
            t.hijoDerecho = self.hijoDerecho
            self.hijoDerecho = t

    def obtenerHijoDerecho(self):
        return self.hijoDerecho

    def obtenerHijoIzquierdo(self):
        return self.hijoIzquierdo

    def asignarValorRaiz(self, obj):
        self.clave = obj

    def obtenerValorRaiz(self):
        return self.clave

r = ArbolBinario('a')
#print('linea40',r.obtenerValorRaiz())
#print('linea41',r.obtenerHijoIzquierdo() )
#r.insertarIzquierdo('b')
#print('linea43',r.obtenerHijoIzquierdo())
#print('linea44',r.obtenerHijoIzquierdo().obtenerValorRaiz())
#r.insertarDerecho('c')
#print('linea46',r.obtenerHijoDerecho())
#print('linea47',r.obtenerHijoDerecho().obtenerValorRaiz())
#r.obtenerHijoDerecho().asignarValorRaiz('hola')
#print('linea47',r.obtenerHijoDerecho().obtenerValorRaiz())
