#ejercicio hecho en clase
#ejercicio 2.4 hecho en clase tambien
 #Ejercicio 2.5 a
print("Dado un numero, 1 es impar 0 es par")
def par_o_impar(num):
    #te dice si el numero es par o impar
    if (num%2==0):
        print("0")
    else:
        print("1")
par_o_impar(4)

#Ejercicio 2.5 b
print("Dado un numero, 1 es par 0 es impar")
def par_o_impar(num):
    #te dice si el numero es par o impar
    if (num%2==0):
        print("1")
    else:
        print("0")
par_o_impar(5)

#Ejercicio 2.5 c
def contador_carac(num):
    #devuelve la cantidad de caracteres de un numero
    cantidad=len(num)
    return(cantidad)
print(contador_carac("2565"))    

#Ejercicio 2.5 d
def mult_de_diez(numero):
    #le doy un numero y me devuelve el mult de 10 mas cercano
    cuenta=(numero//10)*10
    return(cuenta)
print(mult_de_diez(168))