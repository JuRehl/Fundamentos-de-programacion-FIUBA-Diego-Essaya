from ejercicios4guia.ejercicio41 import numero_primo
from ejercicios2guia.ejercicio2_8 import main
#Ejercicio 7.5  a
def es_numero_primo(lista):
    """Te dice que numeros de la lista son primos"""
    lista_filtrada=[]
    for numero in lista:
        if numero_primo(numero):
            lista_filtrada.append(numero)
    return lista_filtrada
lista1=[5,10,7,13,20]
es_numero_primo(lista1)

#Ejercicio 7.5 b
def suma_y_promedio(lista):
    """Te da el promedio y suma de una lista de numeros"""
    suma=0
    for n in lista:
        suma+=n
    promedio=suma/len(lista)
    return suma,promedio

#Ejercicio 7.5 c
def calc_factoriales(lista):
    """Te da los factoriales de los numeros de una lista"""
    res=[]
    for n in lista:
        f=main(n)
        res.append(f)
    return res
