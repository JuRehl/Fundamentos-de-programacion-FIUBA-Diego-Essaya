#Ejercicio1.6 a
def operaciones(num1, num2):
    #funcion que devuelve suma resta multiplicacion y division de dos numeros
    suma= num1+num2
    resta= num1-num2
    multiplicacion=num1*num2
    division=num1/num2
    return(suma,resta,multiplicacion,division)
print(operaciones(2,4))

#Ejercicio 1.6 b
def tabla_mult(num):
    #funcion que le doy un numero y me da su tabla de multiplicacion hasta el 10
    for i in range (0,11):
        multiplicacion= num*i
        print("2x",i, "=",multiplicacion)
print(tabla_mult(2))