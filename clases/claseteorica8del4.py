def buscar(secuencia:list,elemento):
    for i in range(len(secuencia)):
        password=secuencia[i]
        if password==elemento:
            return i
    return -1


#otro ejercicio
def max(L):
    """pre:lista no vacia"""
    max_actual=L[0]
    for i in range(1,len(L)):
#Si la lista tiene un elemento no entra nunca al range
        if L[i]>max_actual:
            max_actual=L[i]
    return max_actual