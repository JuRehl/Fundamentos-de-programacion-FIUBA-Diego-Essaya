def cp(ruta_original,ruta_destino):
    with open(ruta_original,"rb") as origen, open(ruta_destino,"wb") as destino:
        contenido=origen.read(1024)
        while len(contenido)>0:
            destino.write(contenido)
            contenido=origen.read(1024)