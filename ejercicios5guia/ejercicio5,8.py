SALIDA=-1
#Ejercicio 5.8
def main():
    """Le doy un numeros hasta que paro y me dice el promedio, la suma, y cantidad de numeros ingresados"""
    contador_numeros=1
    numero_usuario=int(input("Ingrese numeros naturales: "))
    suma_numeros=numero_usuario
    while numero_usuario>0:
        numero= int(input("Ingrese numeros naturales, -1 si ya ingreso todos: "))
        if numero!=SALIDA:
            suma_numeros+=numero
            contador_numeros+=1
        else:
            numero_usuario=SALIDA
    print("Se ingresaron ", contador_numeros, " numeros")
    print("La suma total de los numeros es: ", suma_numeros)
    print("El promedio de los numeros es: ", suma_numeros/contador_numeros)
main()
