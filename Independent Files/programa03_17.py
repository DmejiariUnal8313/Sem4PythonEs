from programa03_18 import ColaDoble

def verificarPalindromo(cadena):

    colaDobleCaracteres = ColaDoble()
    for caracter in cadena:
        if caracter != " ":
            colaDobleCaracteres.agregar(caracter,"Final")
            colaDoblecaracteres.agregar(caracter,"Frente")
            

    aunIguales = True

    while colaDobleCaracteres.tamano() > 1 and aunIguales:
        primero = colaDobleCaracteres.remover("Frente")
        ultimo = colaDobleCaracteres.remover("Final")
        if primero != ultimo:
            aunIguales = False

    return aunIguales

print(verificarPalindromo("lsdkjfskf"))
print(verificarPalindromo("anita lava la tina"))
