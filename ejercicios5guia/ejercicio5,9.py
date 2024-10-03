#Ejercicio 5.9 a
def multiplos(n1,n2):
    """Le doy dos números y me dice los multiplos entre ellos"""
    multiplos=""
    for i in range (n1,n2):
        if i%n1==0:
            multiplos+=str(i) + " "
            return(multiplos)
multiplos(4,15)

#Ejercicio 5.9 b
def multiplos_bucle(n1,n2):
    """Le doy dos numeros y me dice los multiplos entre ellos hasta q el multiplo sea mayor q el segundo numero"""
    mult=0
    while n1<n2:
        mult+=1
        multiplicacion=n1*mult
        if multiplicacion>n2:
            break
        return multiplicacion
multiplos_bucle(4,15)

#Ejercicio5.9 c
#Comparando las implementaciones la más clara es la primera
#Ya que usamos for y se itera más facil a la hora de ver
#cuales son los numeros multiplos entre un rango especifico
#Además la primera requiere de menos operaciones
