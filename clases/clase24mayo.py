import os
#Fibonacci recursivo
def _fib(n,dicc):
    if n in dicc:
        return dicc[n]
    if not n-1 in dicc:
        dicc[n-1]=_fib(n-1,dicc)
    return dicc[n-1] + dicc[n-2]
#Otra solucion
def fib_memorioso(n,dicc):
    if n not in dicc:
        dicc[n]=fib_memorioso(n-1,dicc)+fib_memorioso(n-2,dicc)
    return dicc[n]

def fib(n):
    dicc={}
    dicc[0]=0
    dicc[1]=1
    return _fib(n,dicc)

#Forma recursiva para archivos dentro de carpetas, devolver todo en un mismo tipo
def listar_rutas(ruta):
    if not os.path.isdir(ruta):
        return [ruta]
    archivos=[]
    for ruta_archivo in os.listdir(ruta):
        ruta_archivo=os.path.join(ruta,ruta_archivo)
        archivos+=listar_rutas(ruta_archivo)
    return archivos

#Ejemplo de recursividad
def particionar(L,es_par):
    if len(L)==0:
        return []
    elemento=L[0]
    resto=L[1:]
    if es_par(elemento):
        return[elemento]+particionar(resto,es_par)
    else:
        return particionar(resto,es_par)+[elemento]
#Otra forma de reselverlo con wrapped
def _particionar(L,f,res,indice):
    if indice>=len(L):
        return 
    elem=L[indice]
    if f(elem):
        res.insert(0,elem)
    else:
        res.append(elem)
    _particionar(L,f,res,indice+1)

def particionar2(L,f):
    res=[]
    _particionar(L,f,res,0)#HAcerlo con res derecha y res izquierda
    return res
