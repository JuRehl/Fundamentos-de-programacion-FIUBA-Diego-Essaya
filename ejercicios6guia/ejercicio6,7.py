#Ejercicio 6,7 a
def encontrar_subcadena(cadena,subcadena):
    """Te dice si una cadena es subcadena de otra"""
    if subcadena in cadena:
        return False
encontrar_subcadena("Juana","Jalkskdn")

#Ejercicio 6,7 b
def anterior_orden_alfabetico(palabra1,palabra2):
    """Te devuelve las que esta antes en orden alfabetico"""
    return min(palabra1,palabra2)
anterior_orden_alfabetico("kde","gnome")