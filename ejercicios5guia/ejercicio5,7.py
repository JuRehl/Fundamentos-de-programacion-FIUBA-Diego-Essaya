#Ejercicio5.7 a
def suma_de_divisores(num):
    contador=0
    for i in range (1,num):
        if num%i==0:
            contador+=int(i)
            print(contador)
            return(contador)
suma_de_divisores(8)

#Ejercicio5.7 b
