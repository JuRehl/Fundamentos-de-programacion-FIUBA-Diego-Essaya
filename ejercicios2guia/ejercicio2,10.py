columnas= int(input("Ingrese la cantidad de numeros de la parte de abajo del domino: "))
filas= int(input("Ingrese la cantidad de numeros de la parte de arriba del domino: "))
def mostrar_coords ():
    """Imprime matriz con todas las coordenadas"""
    
    for i in range (filas+1):
        for c in range (columnas +1):
            print(str(i) + "," + str(c), end= "  ")
        print()

mostrar_coords()

