import struct

#Ejercicio 11.6 c
def guardar_numeros(ruta_destino,numeros):
    with open(ruta_destino, "wb") as destino:
        for n in numeros:
            contenido=struct.pack(">i", n)
            destino.write(contenido)

def cargar_numero(ruta):
    numeros=[]
    with open(ruta, "rb") as archivo:
        while True:
            contenido=archivo.read(4)
            if len(contenido)==0:
                break
            n=struct.unpack(">i", contenido)[0]
            numeros.append(n)
    return numeros
