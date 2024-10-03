#Ejercicio 15.6
def calcular_triangular(n):
    if n==1:
        return 1
    return n + calcular_triangular(n-1)
