miLista = [1,2,3,4]
A = [miLista]*3
print(A)

miLista[2]=45
print(A)

miLista[2]=3
B=list(miLista)
print(B)

miLista[2]=45
print([B]*3)
