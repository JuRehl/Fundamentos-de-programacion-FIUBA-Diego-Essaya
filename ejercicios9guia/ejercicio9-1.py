#Ejercicio 9.1
def tuplas_a_diccionario(l):
    diccionario_segun_tuplas={}
    nueva_frase=[]
    nueva_key=[]
    for i in range(len(l)):
        if not l[i][0] in nueva_key:
            nueva_key.append(l[i][0])
    for k in nueva_key:
        lista_palabras=[]
        for j in range(len(l)):
            if l[j][0]==k:
                lista_palabras.append(l[j][1])
        nueva_frase.append(lista_palabras)
    for m in range(len(nueva_key)):
        diccionario_segun_tuplas[nueva_key[m]]=nueva_frase[m]
    return diccionario_segun_tuplas
tupla_ejemplo=[ ('Hola', 'don Pepito'), ('Hola', 'don Jose'),('Buenos', 'días') ]
print(tuplas_a_diccionario(tupla_ejemplo))            