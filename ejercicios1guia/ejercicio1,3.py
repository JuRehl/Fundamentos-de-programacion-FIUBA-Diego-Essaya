#Ejercicio 1.3 a
def periemtro_rectan(base,altura):
    #calcula el perimetro de un rectangulo
    return(2*(base+altura))
print(periemtro_rectan(2,4))

#Ejercicio 1.3 b
def area_rect(base,altura):
    #calcula el area de un rectangulo
    return(base*altura)
print(area_rect(4,2))

#Ejercicio 1.3 c
def area_rect_alineadoxy(x1,x2,y1,y2):
    #area de un rectangulo alineado con los ejes x y
    #en este caso (x1,y1) va a ser la base (x2,y2) va a ser la altura
    return(x1*y2)
print(area_rect_alineadoxy(4,0,0,2))

#Ejercicio 1.3 d
import math
def perimetro_circulo(radio):
    #dado el radio de un circulo te calcula el perimetro
    return(math.pi*(radio*2))
print(perimetro_circulo(5))

#Ejercicio 1.3 e
def area_circulo(radio):
    #le doy el radio de un circulo devuelve el area
    return(math.pi*(radio**2))
print(area_circulo(5))

#Ejercicio 1.3 f
def volumen_esfera(radio):
#le doy el radio y calcula volumen de una esfera
    return((4/3)*math.pi*(radio**3))
print(volumen_esfera(5))

#Ejercicio 1.3 g
def hipot_triangulorect(cat1,cat2):
    """Calcula hipotenusa"""
    adentro= (cat1**2)+(cat2**2)
    raiz=math.sqrt(adentro)
    return(raiz)
print(hipot_triangulorect(4,5))

#Para importar un archivo que hemos hecho, debemos poner import (nombre del archivo) y ponerla funcion que necesitamos, al principio del código
#Un programa tiene input y print