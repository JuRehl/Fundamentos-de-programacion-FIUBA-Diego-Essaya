#Ejercicio4.4 a
def max_min_polinomio2(a,b,c):
    """Le doy valores de poliniomio grado 2 y me da su min o max"""
    valor_en_x= -1*(b/2*a)
    valor_en_y=c-((b**2)/4*a)
    if a > 0:
        return (valor_en_x, valor_en_y)
    else:
        return(valor_en_x,valor_en_y)
max_min_polinomio2(-1,2,-1)

#Ejercicio 4.4 b
import math
def raices_polinomio(a,b,c):
    """Hace bhaskara"""
    while (a!=0):
        dentro_raiz= (b**2)-(4*a*c)
        raiz = math.sqrt(dentro_raiz)
        if dentro_raiz>0:
            parte_arriba_positiva= (-b + raiz)
            parte_arriba_negativa= (-b - raiz)
            raiz_positiva= parte_arriba_positiva/(2*a)
            raiz_negativa=parte_arriba_negativa/(2*a)
            return(raiz_positiva,raiz_negativa)
        else:
            return False
        return(False)
raices_polinomio(1,3,-4)

#Ejercicio 4.4 c
