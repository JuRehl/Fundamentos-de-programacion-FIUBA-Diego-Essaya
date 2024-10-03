#Ejemplo de uso MAP
"""map(factorial,[1,2,3,4]) -->[factorial(1),factorial(2),...]
para convertirlo en lista 
igualamos map en una variable por ejemplox y colocamos list(x)"""
#Ejemplo de uso FILTER
"""filter(es_primo, [1,2,3,4,5,7,....]) --> [1,3,5,7] cambia segun True or False"""
#Funciones en variables
"""para una funcion x=funcion sin los parentesis xq sino nos dice que x vale 
lo que devuelva la funcion: Luego invocamos x() con los  parametros de la funcion """
#[<expresion> for <var> in <secuencia>]
#[i for i in range(500)] --> te da una lista hasta el 499
#[0 for i in range(500)] --> te da una lista con 499 ceros
"""i se puede usar tanto en condicion como expresion, te da como resultado una lista"""
print([i for i in range(10) if i%2==0])