#Ejercicio 15.5
def impar(n):
    if n==1:
        return True
    return par(n-1)

def par(n):
    if n==1:
        return False
    return impar(n-1)



