#Ejercicio 7.2 a
def fichas_encajan_o_no(ficha1, ficha2):
    """Te dice en donde encajan las fichas de un domino"""
    if ficha1[0]==ficha2[0]:
        print("Las fichas", ficha1, "y", ficha2, "encajan en", ficha1[0] ,"y", ficha2[0])
    elif ficha1[0] == ficha2[1]:
        print("Las fichas", ficha1, "y", ficha2, "encajan en", ficha1[0] ,"y", ficha2[1])
    elif ficha1[1]==ficha2[0]:
        print("Las fichas", ficha1, "y", ficha2, "encajan en", ficha1[1] ,"y", ficha2[0])
    elif ficha1[1]==ficha2[1]:
        print("Las fichas", ficha1, "y", ficha2, "encajan en", ficha1[1] ,"y", ficha2[1])
    else:
        print("Las fichas no encajan")
ficha1_ejemplo= (3,4)
ficha2_ejemplo= (5,4)
fichas_encajan_o_no(ficha1_ejemplo,ficha2_ejemplo)

#Ejercicios 7.2 b
def fichas_encajan_o_no_str(ficha1, ficha2):
    """Te dice en donde encajan las fichas de un domino se da las fichazs en str y separa"""
    ficha1_cambiada=tuple(ficha1.split("-"))
    ficha2_cambiada=tuple(ficha2.split("-"))
    if ficha1[0]==ficha2[0]:
        print("Las fichas", ficha1_cambiada, "y", ficha2_cambiada, "encajan en", ficha1_cambiada[0] ,"y", ficha2_cambiada[0])
    elif ficha1[0] == ficha2[1]:
        print("Las fichas", ficha1_cambiada, "y", ficha2_cambiada, "encajan en", ficha1_cambiada[0] ,"y", ficha2_cambiada[1])
    elif ficha1[1]==ficha2[0]:
        print("Las fichas", ficha1_cambiada, "y", ficha2_cambiada, "encajan en", ficha1_cambiada[1] ,"y", ficha2_cambiada[0])
    elif ficha1[1]==ficha2[1]:
        print("Las fichas", ficha1_cambiada, "y", ficha2_cambiada, "encajan en", ficha1_cambiada[1] ,"y", ficha2_cambiada[1])
    else:
        print("Las fichas no encajan")
ficha1_ejemplo= "3-4"
ficha2_ejemplo= "5-4"
fichas_encajan_o_no_str(ficha1_ejemplo,ficha2_ejemplo)
