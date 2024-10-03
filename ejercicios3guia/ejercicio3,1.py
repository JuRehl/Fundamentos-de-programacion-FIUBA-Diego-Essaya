#Ejercicio 3.1 a
def calcular_en_segundos (horas, minutos, segundos):
    if horas==horas+ "hs":
        print("En segundos es: ", horas*3600)
    elif minutos== minutos+ "min":
        print("En segundos es: ", minutos* 60)
    else:
        print("Has ingresado la hora en segundos, queda igual: ", segundos)

calcular_en_segundos("5hs", 5, 1)