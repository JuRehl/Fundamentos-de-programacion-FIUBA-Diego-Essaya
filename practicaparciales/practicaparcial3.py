
import random
def eliminar_pares(lista, indice):
    if indice >len(lista)-1:
        return lista
    if lista[indice]%2==0:
        lista.pop(indice)
        if indice==0:
            indice=0
        else:
            indice-=1
    else:
        indice+=1
    return eliminar_pares(lista, indice)

def _cant_carac(c,s,contador):
    if len(s)==0:
        return contador
    caracter=s[0]
    if caracter==c:
        contador+=1
    s=s[1:]
    return _cant_carac(c,s,contador)

def cant_carac(c,s):
    contador=0
    return _cant_carac(c,s,contador)

def _suma_elementos(lista1,lista2,lista_final,indice):
    if len(lista2)==indice:
        return lista_final
    result=lista1[indice]+lista2[indice]
    lista_final.append(result)
    indice+=1
    return _suma_elementos(lista1,lista2,lista_final,indice)

def suma_elementos(lista1,lista2):
    if len(lista1)>len(lista2) or len(lista1)==len(lista2):
        return _suma_elementos(lista1,lista2,[],0)
    elif len(lista1)<len(lista2):
        return _suma_elementos(lista2,lista1,[],0)

def suma_digital(num):
    if num<10:
        return num
    return num%10 + suma_digital(num//10)

def partido(contador_a,contador_b,contador_g):
    if contador_a==3:
        return "Alan"
    if contador_b==3:
        return "Bárbara"
    if contador_g==3:
        return "Grace"
    jugadores=["Alan","Grace","Bárbara"]
    jugando=["Alan", "Bárbara"]
    perdedor=random.choice(jugando)
    jugando.remove(perdedor)
    if "Alan" in jugando:
        contador_a+=1
    elif "Bárbara" in jugando:
        contador_b+=1
    elif "Grace" in jugando:
        contador_g+=1
    if "Alan"==perdedor:
        contador_a=0
    elif "Bárbara"==perdedor:
        contador_b=0
    elif "Grace"==perdedor:
        contador_g=0
    for jugador in jugadores:
        if jugador not in jugando and jugador!=perdedor:
            jugando.append(jugador)
    return partido(contador_a,contador_b,contador_g)

def _replicar(lista,n,cont_indices):
    if cont_indices==len(lista)-1:
        return lista
    for i in range(n-1):
        variable=lista[cont_indices]
        lista.insert(cont_indices,variable)
    cont_indices+=n
    return _replicar(lista,n,cont_indices)
def replicar(lista,n):
    contador=0
    return _replicar(lista,n,contador)

def _es_palindromo(cadena,nueva_cad,contador):
    if len(nueva_cad)==len(cadena):
        if "".join(nueva_cad)==cadena:
            return True
        else:
            return False
    caracter=cadena[contador]
    nueva_cad.append(caracter)
    contador-=1
    return _es_palindromo(cadena,nueva_cad,contador)
def es_palindromo(cadena):
    nueva_cadena=[]
    contador=len(cadena)-1
    return _es_palindromo(cadena, nueva_cadena,contador)

def collatz(n):
    if n==1:
        return 1
    if n%2==0:
        print(n//2)
        return collatz(n//2)
    else:
        print((n*3)+1)
        return collatz((n*3)+1)

def _cantidad_caracter(cadena,contador,caracter):
    if len(cadena)==0:
        return contador
    if cadena[0].lower()==caracter:
        contador+=1
    cadena=cadena[1:]
    return _cantidad_caracter(cadena,contador,caracter)
def cantidad_caracter(cadena):
    contador=0
    caracter=cadena[0].lower()
    return _cantidad_caracter(cadena[1:],contador,caracter)

def es_par(n):
    if n%2==0:
        return True
    return False
def _particionar(L,f,nueva_lista):
    if len(L)==0:
        return nueva_lista
    elemento=L[0]
    if f(elemento):
        nueva_lista.insert(0,elemento)
        return _particionar(L[1:],f,nueva_lista)
    else:
        nueva_lista.append(elemento)
        return _particionar(L[1:],f,nueva_lista)

def particionar(L,f):
    lista=[]
    return _particionar(L,f,lista)

def eliminar_pares(L):
    if len(L)==0:
        return []
    elemento=L[0]
    if elemento%2!=0:
        return [elemento]+eliminar_pares(L[1:])
    else:
        return eliminar_pares(L[1:])

def _producto_indices(L,nueva_L):
    if len(L)==0:
        return nueva_L
    elemento=L[0]
    if len(nueva_L)==0:
        nueva_L.append(elemento)
    else:
        nueva_L.append(elemento*nueva_L[-1])
    return _producto_indices(L[1:],nueva_L) 
def producto_indices(lista):
    lista_nueva=[]
    return _producto_indices(lista,lista_nueva)

    
def invertir_cadena(cadena):
    if len(cadena)==0:
        return ""
    elemento=cadena[-1]
    return elemento + invertir_cadena(cadena[0:len(cadena)-1])


def potencia(base,exponente):
    if exponente==0:
        return 1
    return base*potencia(base,exponente-1)

def cuenta_regresiva(num):
    if num==-1:
        return -1
    print(num)
    return cuenta_regresiva(num-1)

def encontrar_valor(lista,valor):
    if len(lista)==0:
        return False
    elemento=lista[0]
    if elemento==valor:
        return True
    return encontrar_valor(lista[1:],valor)

def validar_parentesis(cadena):
    if len(cadena)==0:
        return True
    elemento1=cadena[0]
    elemento2=cadena[-1]
    if elemento1!="(" or elemento2!=")":
        return False
    return validar_parentesis(cadena[1:len(cadena)-1])