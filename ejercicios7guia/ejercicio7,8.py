#Ejercicio7.8 a
def invertir_lista(lista):
    for i  in range(len(lista)//2):
        aux=lista[len(lista)-i-1]
        lista[len(lista)-i-1]=lista[i]
        lista[i]=aux
    return lista
lista1=[3,4,7,9,12,1]
print(invertir_lista(lista1))

#Ejercicio 7.8 b
def invertir_lista_modificando(lista):
    for i in range(len(lista)):
        lista[i],lista[len(lista) -i -1]=lista[len(lista) -i- 1],lista[i]
    return lista
print(invertir_lista_modificando(lista1))
