#Ejercicio 5.2
from ejercicios4guia.ejercicio41 import numero_primo

def descom_en_primos(n):
    """Le doy un número y me dice los numeros primos que hay hasta el número"""
    while n>1:
        for i in range(2,n+1):
            if numero_primo(i):
                return i
        return False
descom_en_primos(25)