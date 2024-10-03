def rot13(ruta_origen,ruta_destino):
    with open(ruta_origen,"r") as archivo_origen, open(ruta_destino,"w") as archivo_destino:
        for linea in archivo_origen:
            linea=0