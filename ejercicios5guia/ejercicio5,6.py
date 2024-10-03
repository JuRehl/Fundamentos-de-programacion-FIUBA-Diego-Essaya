#Ejercicio5.6 a
import math
def es_potencia_de_dos(n):
    """Me dice si n es potencia de 2"""
    resto=math.log2(n)
    for i in range (1,1000):
        if resto==1:
            print(i)
            return True
        return False
es_potencia_de_dos(8)

#Ejercicio 5.6 b
def es_potencia_de_dos_rango(n1,n2):
    """Me dice si n es potencia de 2 entre el rango del parámetro"""
    for num in range (n1,n2):
        suma_pot_2=""
        if es_potencia_de_dos(num):
            suma_pot_2+=str(num)
            continue
        else:
            suma_pot_2=0 
    print(suma_pot_2)
es_potencia_de_dos_rango(1,8)



