VECTOR1=(1,2)
VECTOR2=(3,4)
from math import sqrt

#Ejercicio 7.4 a
def prod_escalar(v1,v2):
    """Te da el producto escalar de dos vectores"""
    prod_componente_x= v1[0]*v2[0]
    prod_componente_Y=v1[1]*v2[1]
    producto=prod_componente_x+prod_componente_Y
    return producto
prod_escalar(VECTOR1,VECTOR2)

#Ejercicio 7.4 b
def vectores_ortogonales(v1,v2):
   """Te dice si dos vectores son ortogonales"""
   prod_componente_x= v1[0]*v2[0]
   prod_componente_Y=v1[1]*v2[1]
   producto=prod_componente_x+prod_componente_Y
   if producto==0:
       return True
vectores_ortogonales(VECTOR1,VECTOR2)

#Ejercicio 7.4 c
def vectores_paralelos(v1,v2):
    """Te dice si dos vectores son paralelos"""
    fraccion1=v1[0]/v2[0]
    fraccion2=v1[1]/v2[1]
    if fraccion1==fraccion2:
        return True
vectores_paralelos(VECTOR1,VECTOR2)

#Ejercicio 7.4 d
def norma_de_un_vector(v1):
    """Te dice la norma de un vector"""
    primero=v1[0]**2
    segundo=v1[1]**2
    adentro_raiz=primero+segundo
    raiz= sqrt(adentro_raiz)
    return raiz
norma_de_un_vector(VECTOR1)
