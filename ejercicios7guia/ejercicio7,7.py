#Ejercicio 7.7
def nombres_y_apellidos(lista):
    """Le doy una lista con tuplas que contienen el 
    nombre apellido e inicial del segundo noombre y 
    me devuelve unido en una cadena"""
    listamodif=[]
    for persona in lista:
        info=persona[0]+ " " +persona[2]+"."+" "+persona[1]
        listamodif.append(info)
    return listamodif
lista1=[("Juana","Rehl","L"), ("Silvina","Vazquez","L"),("Juan","Rehl","A")]
print(nombres_y_apellidos(lista1))
