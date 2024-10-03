#Ejercicio de Discord
def actores_poranio(direccion):
    resultado={}
    with open(direccion, "r") as archivo:
        archivo.readline()
        for linea in archivo: #-> reader=csv.reader(archivo,delimiter ";") con import csv
            linea=linea.rstrip()
            partes=linea.split(";") #-> for linea in reader con import csv
            pelicula,anio,actores=partes
            if not anio.isdigit():
                continue
            actores=actores.split(",")
            for actor in actores:
                if not actor in resultado:
                    resultado[actor]=[]
                resultado[actor].append(int(anio))
        return resultado
        
#Importante para tp2
def main():
    ruta=input("Ingrese la ruta: ")
    try:
        actores=actores_poranio(ruta)
        print(actores)
    except FileNotFoundError:
        print("Archivo no encontrado")


#Ejercicio parcial
def gimnasio_mas_cercano(gimnasios,x,y):
    """Funcion auxiliar"""
    dist_min=None
    gim_min=None
    for gim in gimnasios:
        g_x,g_y=gimnasios[gim]
        dist=abs(x-g_x)+abs(y-g_y)
        if dist_min is None or dist<dist_min:
            dist_min=dist
            gim_min=gim
    return gim_min

def pokemones_mas_cercanos(ruta_pokemones,gimnasios,ruta_destino):
    """Para hacer procesamiento y escritura"""
    with open(ruta_pokemones, "r") as archivo_origen, open(ruta_destino,"w") as archivo_destino: #abrir dos archivos a la vez
        for linea in archivo_origen:
            linea=linea.strip()
            pokemon,tipo,coordenadas=linea.split(",")
            x,y=coordenadas.split(",")
            x,y=int(x),int(y)
            gimnasio=gimnasio_mas_cercano(gimnasios,x,y)
            archivo_destino.write(f"{pokemon};{tipo};{gimnasio}\n")


