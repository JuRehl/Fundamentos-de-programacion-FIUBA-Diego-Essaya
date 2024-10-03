#Ejercicio 8.1 a
def coincidencias(lista_desordenada, elemento):
    """Me da la cantidad de elementos de una lista que coinciden con el elemento"""
    contador=0
    for elementos in lista_desordenada:
        if elemento==elementos:
            contador+=1
    return contador
lista1=[5,3,4,7,8,2,5,1,6]

#Ejercicio 8.1 b
def primer_elemento_igual_a_elementos(lista_desordenada, elemento):
    """Le doy una lista y un elemento y me da el primer valor de la lista que coincide con el elemento(solo la posicion)"""
    for elementos in lista_desordenada:
        if elemento==elementos:
            posicion=lista_desordenada.index(elementos)
            return posicion
        
#Ejercicio 8.1 c
def primer_elemento_igual_a_elementos_varios(lista_desordenada, elemento):
    """Le doy una lista y un elemento y me devuelve los valores de la lista que coinciden con el elemento(solo la posicion)"""
    lista_posiciones=[]
    for i, elementos in enumerate(lista_desordenada):
        if elemento==elementos:
            lista_posiciones.append(i)
    return lista_posiciones
print(primer_elemento_igual_a_elementos_varios(lista1,5))
            

