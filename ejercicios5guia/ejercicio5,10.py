#Ejercicio 5.10
from ejercicios4guia.ejercicio41 import numero_primo
def numero_primo_en_un_rango(n):
    for i in range (2,n):
        primos=numero_primo(i)
        print(primos)
numero_primo(6)