def wc(ruta):
    lineas=0
    caracteres=0
    palabras=0
    with open(ruta,"r") as archivo:
        for linea in archivo:
            linea=linea.strip()
            lineas+=1
            for caracter in linea:
                caracteres+=1
            linea=linea.split()
            palabras+=len(linea)
        return lineas,caracteres,palabras
