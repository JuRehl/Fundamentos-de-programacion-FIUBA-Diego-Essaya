#Ejercicio 8.2 a
def valor_max_lista(lista):
    """Te da el valor maximo d euna lista"""
    maximo=max(lista)
    return maximo
lista1=[1,5,7,15,4,8,9,36,5]

#Ejercicio 8.2 b
def valor_max_y_posicion(lista):
    """Te da el valor maximo de una lista y su posicion"""
    maximo=max(lista)
    for i, elementos in enumerate(lista):
        if maximo==elementos:
            posicion=i
    tupla=(maximo,posicion)
    return tupla

#Ejercicio 8.2 c
def valor_max_pos_cadena(lista):
    """De una lista de cadenas te da la mas larga y su posicion"""
    cadena_en_numeros=map(len,lista)
    longitudes=list(cadena_en_numeros)
    maximo=max(longitudes)
    for i, long in enumerate(longitudes):
        if maximo==long:
            posicion=i
    cadena=lista[posicion]
    tupla=(cadena,i)
    return tupla
lista2=["Hola", "Juana", "Silvina"]
print(valor_max_pos_cadena(lista2))

