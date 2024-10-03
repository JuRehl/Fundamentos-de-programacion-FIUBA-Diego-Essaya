import random
#Ejercicio 15.2
def experimento(contador):
    opcion=random.randint(1,3)
    print(opcion)
    if opcion==3:
        return 7+contador
    elif opcion==2:
        contador+=5
        return experimento(contador)
    elif opcion==1:
        contador+=3
        return experimento(contador)
contador=0