def grep(ruta,cadena):
    with open(ruta,"r") as archivo:
        for linea in archivo:
            linea=linea.strip()
            if cadena in linea:
                print(linea)

