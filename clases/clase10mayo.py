import struct

FORMATO=">i3sF"
estudiantes=[(101696, "JDS",7,5), (104733,"ABR",9.0)]

def guardar_estudiantes(estudiantes, ruta):
    with open(ruta, "wb") as archivo:
        for padron,iniciales,promedio in estudiantes:
            contenido=struct.pack(FORMATO,padron,iniciales.encode(),promedio) #hay que mandarle la cadena en bytes, facilita
            archivo.write(contenido)

def cargar(ruta):
    estudiantes=[]
    with open(ruta, "rb") as archivo:
        cantidad=struct.calcsize(FORMATO)
        while True:
            contenido=archivo.read(cantidad)
            if len(contenido)==0:
                break
            padron,iniciales,promedio=struct.unpack(FORMATO,contenido)
            iniciales=iniciales.decode()
            estudiantes.append(padron,iniciales,promedio)
    return estudiantes
