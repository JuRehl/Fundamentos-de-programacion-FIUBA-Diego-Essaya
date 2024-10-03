#Ejercicio 11.7 a
def cargar__datos(ruta):
    res={}
    with open(ruta, "r") as archivo:
        for linea in archivo:
            linea=linea.strip()
            clave,valor=linea.split(",")
            res[clave]=res.get(clave,[])
            res[clave].append(valor)
        return res
datos=cargar__datos("archivo.txt")


#Ejercicio 11.7 b
def guardar_datos(datos,ruta):
    with open(ruta, "w") as archivo:
        for clave in datos:
            valores=datos[clave]
            for valor in valores:
                archivo.write(
                    f"{clave}, {valor} \n"
                )

