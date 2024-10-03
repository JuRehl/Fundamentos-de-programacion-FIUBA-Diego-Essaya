#Ejercicio 7.6 a
def filtros_de_listaen_funcion_de_k(lista,k):
    """Te da listas con los numeros mayoes,menores e iguales a k"""
    listamenores=[]
    listamayores=[]
    listaiguales=[]
    for numero in lista:
        if numero>k:
            listamayores.append(numero)
        elif numero<k:
            listamenores.append(numero)
        else:
            listaiguales.append(numero)
    return listamayores,listamenores,listaiguales
lista1=[2,8,4,6,7,14,-2,5]

#Ejercicio 7.6 b
def multiplos_de_k(lista,k):
    """Te da una lista con los numeros de una lista que son multiplos de k"""
    listamultiplos=[]
    for numero in lista:
        if numero%k==0:
            listamultiplos.append(numero)
    return listamultiplos

