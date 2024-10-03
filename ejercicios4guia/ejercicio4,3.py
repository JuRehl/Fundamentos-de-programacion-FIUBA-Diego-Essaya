columnas= int(input("ingrese la cantidad de columnas de la matriz "))
filas= int(input("Ingrese la cantidad de filas de la matriz "))
def crear_matriz():
    for f in range(1,filas+1):
        for c in range(1,columnas+1):
            print("M", end= " ")
        print()
crear_matriz()