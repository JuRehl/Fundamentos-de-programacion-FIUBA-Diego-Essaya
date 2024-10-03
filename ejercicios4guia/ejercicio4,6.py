#Ejercicio 4.6
def que_dia_es (dia):
    if dia%4==0:
        print("Jueves")
    elif dia%6==0 and not dia%3==0:
        print("Sábado")
    elif dia%2==0:
        print("Martes")
    elif dia%5==0:
        print("Viernes")
    elif dia%3==0:
        print("Miércoles")
    elif dia%7==0:
        print("Domingo")
    else:
        print("Lunes")
que_dia_es(1)