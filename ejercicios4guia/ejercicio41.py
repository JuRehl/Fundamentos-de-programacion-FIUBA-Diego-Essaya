#Ejercicio 4.1 a
def numero_par(num):
    """Me dice si el numero es par"""
    if num%2==0:
        return(True)

#Ejercicio 4.1 b
def numero_primo(numero):
    """Me dice si es primo o no"""
    for n in range(2,numero):
        if numero%n==0:
            return False
        return True
