#Ejercicio 7.3 a
def campaña_votantes(nombres):
    """Te dice estimado nombre de tupla vote por mi"""
    for nombre in nombres:
        print(f"Estimado {nombre} vote por mi")
nombres_ejemplo=("Juana","Taylor", "Boquita")
campaña_votantes(nombres_ejemplo)

#Ejercicio 7.3 b
def campaña_votantes(nombres,p,n):
    """Misma funcion que la anterior pero empezando en p y se hace n cantidad de veces"""
    for nombre in nombres[p:p+n]:
        print(f"Estimado {nombre} vote por mi")
nombres_ejemplo=("Juana","Taylor", "Boquita","Letis")
campaña_votantes(nombres_ejemplo,2,3)

#Ejercicio 7.3 c
def campaña_votantes(nombres):
    """Misma funcion que la a pero con genero en estimadx"""
    for nombre in nombres:
        if nombre[1]=="mujer":
            print(f"Estimada {nombre[0]} vote por mi")
        else:
            print(f"Estimado {nombre[0]} vote por mi")
    return False
nombres_ejemplo=(("Juana", "mujer"),("Taylor", "mujer"), ("Boquita", "hombre"))
campaña_votantes(nombres_ejemplo)

def campaña_votantes(nombres,p,n):
    """Misma funcion que la b pero con genero en estimadx"""
    for nombre in nombres[p:p+n]:
        if nombre[1]=="mujer":
            print(f"Estimada {nombre[0]} vote por mi")
        else:
            print(f"Estimado {nombre[0]} vote por mi")
nombres_ejemplo=(("Juana","mujer"),("Taylor","hombre"), ("Boquita", "hombre"),("Letis", "hombre"))
campaña_votantes(nombres_ejemplo,2,3)
