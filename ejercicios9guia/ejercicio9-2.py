import random

#Ejercicio 9.2 a
def contar_palabras(cadena):
    nuevo_diccionario={}
    keys=[]
    lista_cadena=cadena.split()
    for i in range(len(lista_cadena)):
        if i==0 or lista_cadena[i]not in keys:
            keys.append(lista_cadena[i].lower())
    lista_contador=[]
    for key in keys:
        contador=0
        for i in range(len(lista_cadena)):
            if lista_cadena[i].lower()==key:
                contador+=1
        lista_contador.append(contador)
    print(lista_contador)
    for j in range(len(keys)):
        nuevo_diccionario[keys[j]]=lista_contador[j]
    return nuevo_diccionario
#print(contar_palabras("Que lindo dia que hace hoy"))

#Ejercicio 9.2 b
def contar_caracter(cadena):
    nuevo_diccionario={}
    keys=[]
    for i in range(len(cadena)):
        if i==0 or cadena[i]not in keys:
            keys.append(cadena[i].lower())
    lista_contador=[]
    for key in keys:
        contador=0
        for i in range(len(cadena)):
            if cadena[i].lower()==key:
                contador+=1
        lista_contador.append(contador)
    print(lista_contador)
    for j in range(len(keys)):
        nuevo_diccionario[keys[j]]=lista_contador[j]
    return nuevo_diccionario
#print(contar_caracter("Que lindo día que hace hoy"))

#Ejercicio 9.2 c
def lanzamiento_dados(cantidad):
    totales={2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
    
    for i in range(cantidad):
        dado1=random.randint(1,6)
        dado2=random.randint(1,6)
        suma=dado1+dado2
        totales[suma]+=1
    return totales
print(lanzamiento_dados(50))