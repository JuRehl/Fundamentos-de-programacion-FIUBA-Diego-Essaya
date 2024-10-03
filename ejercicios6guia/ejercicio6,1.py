#Ejercicio 6.1 a
def dos_cracteres(palabra):
    """Te imprime los primeros dos caracteres"""
    print(palabra[0:2])
dos_cracteres("hola")

#Ejercicio 6.1 b
def tres_ult_carac(palabra):
    """Te imprime los tres ultimos caracteres"""
    print(palabra[-3:])
tres_ult_carac("hola")

#Ejercicio6.1 c
def cada_dos_carac(palabra):
    """Te imprime cada dos caracteres"""
    print(palabra[::2])
cada_dos_carac("recta")
#Este tipo de metodo (usar rangos en cadenas) nunca te tira error como mucho una cadena vacia

#Ejercicio 6.1 d
def cadena_inversa(palabra):
    """Te da la cadena en orden inverso"""
    print(palabra[::-1])
cadena_inversa("Hola mundo!")
#otra forma (vista en clase)
def imprimir_invertido(palabra):
    for i in range(len(palabra)-1, -1, -1):
        print(palabra[i], end="")
imprimir_invertido("recta")

#Ejercicio 6.1 e
def inverso_y_normal(palabra):
    """Te da la cadena inversa y normal"""
    print(palabra + palabra[::-1])
inverso_y_normal("reflejo")