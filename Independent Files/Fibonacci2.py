lista = []
def Fibonacci(n):
    lista.append(1)
    if n < 2:
        return n
    else:
        print("F",n-1,"+F",n-2)
        return Fibonacci(n-1) + Fibonacci(n-2)

Fibonacci(8)
print(sum(lista))
