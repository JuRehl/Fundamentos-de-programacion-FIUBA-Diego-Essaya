#Ejercicio 11.1 visto en clase
def head(nombre_archivo,N):
    with open(nombre_archivo, "r") as archivo: #Siempre usar with para que se cierre automáticamente
        for linea in archivo:
            linea=linea.strip()#Siempre utilizarlo para eliminar los saltos de linea
            print(linea)
            N-=1
            if N<=0:
                return
            
"""Variacion del ejercicio"""
def tail(direccion,n):
    """Se llama sliding window (este metodo) para tp2"""
    lineas=[]
    with open(direccion, "r") as archivo:
        for linea in archivo:
            lineas.append(linea)
            if len(lineas)>n:
                lineas.pop(0)
    for linea in lineas:
        linea=linea.rstrip()
        print(linea)
