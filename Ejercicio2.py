#Emmanuel Diaz Vera
def factorial(n): #definimos una función llamada factorial que depende de un número n
    if n== 0 or n == 1: #esta función nos sirve por si ingresamos 0 o 1 de primer valor
        return 1
    else: 
        return n*factorial(n-1)

n= factorial(10)
print(n)        