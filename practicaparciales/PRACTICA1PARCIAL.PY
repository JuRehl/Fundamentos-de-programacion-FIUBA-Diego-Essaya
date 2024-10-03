def numeros(lista, n):
    contador=0
    for i in range(len(lista)):
        print(lista[i], end= " ")
        contador+=1
        if contador%n==0:
            print()
        
#lista1=[1,2,3,4,5,6]

def validar_contraseña(palabra,n):
    contador=0
    while contador!=n:
        contraseña=input("Ingrese la contaseña: ")
        if contraseña==palabra:
            return True
        else:
            contador+=1
    return False

def validar_contraseña(n):
    contador=0
    while contador!=n:
        contraseña=input("Ingrese la contraseña: ")
        contador_numeros=0
        contador_letras=0
        for l in contraseña:
            if l.isdigit():
                contador_numeros+=1
            elif l.isalpha():
                contador_letras+=1
            else:
                continue
        contador_simbolos=0
        for s in contraseña:
            if "!"==s:
                contador_simbolos+=1
            elif "@"==s:
                contador_simbolos+=1
            elif "~"==s:
                contador_simbolos+=1
            elif "/"==s:
                contador_simbolos+=1
            elif "#" ==s:
                contador_simbolos+=1
        if contador_numeros<contador_letras and contador_simbolos!=0 and contador_simbolos<4:
            print("contraseña correcta")
            return (n-contador)
        else:
            print("Contaseña incorrecta")
            contador+=1
    print("Se acabaron los intentos")
    return-1

def lista_en_un_rango():
    while True:
        numero1=input("Ingrese el primer numero: ")
        numero2=input("Ingrese el segundo numero: ")
        if not numero1.isdigit():
            continue
        if not numero2.isdigit():
            continue
        if numero2<numero1:
            continue
        else:
            break
    lista_en_rango=[]
    numero1 and numero2
    for num in range(int(numero1),int(numero2)+1):
        lista_en_rango.append(num)
    lista_pares=[]
    for numeros in lista_en_rango:
        if numeros%2==0:
            lista_pares.append(numeros)
    return lista_pares

def desbloquear_caja_fuerte(contraseña,intentos):
    cantidad_intentos=0
    contador_digitos=0
    contraseña_valida=""
    while cantidad_intentos<intentos:
        contraseña_usuario=input("Ingrese un digito: ")
        if contraseña_usuario!=contraseña[contador_digitos]:
            print("El digito no corresponde")
            cantidad_intentos+=1
            contraseña_valida=""
            contador_digitos=0
            continue
        else:
            contraseña_valida+=contraseña_usuario
            contador_digitos+=1
            if contraseña_valida==contraseña:
                return True
            else:
                continue
    return False

import random
def generar_direccion_ipvg():
    cadena_nueva=""
    cadena_caracteres="0123456789abcdef"
    contador_separador=0
    for i in range(32):
        letra=random.choice(cadena_caracteres)
        cadena_nueva+=letra
        contador_separador+=1
        if contador_separador%4==0:
            if i==31:
                continue
            else:
                cadena_nueva+=":"
            letra=""
        else:
            letra=""
    return cadena_nueva

def alumno_en_practica(lista,practica):
    alumnos_practica=[]
    for alumno in lista:
        nombre=""
        if alumno[3]==practica:
            nombre+=alumno[1]
            nombre+=" "
            nombre+=alumno[2]
            alumnos_practica.append(nombre)
    return alumnos_practica
alumnos= [(103456, "Juan", "Pérez", "Grace"), (103333, "Marta", "López", "Bárbara"), (103692, "Diana", "Rodríguez", "Grace"), (99264, "Pepito", "Martínez", "Alan")]

def obtener_bigramas(texto):
    bigramas=[]
    palabras =texto.split(" ")
    for i in range(len(palabras)-1):
        palabra1= palabras[i]
        palabra2=palabras[i+1]  
        bigramas.append((palabra1,palabra2))
    return bigramas

#Ejercicio taller 1
def numeros_terminados_en_cero(lista):
    numeros_cero=[]
    for num in lista:
        if str(num)[-1]=="0":
            numeros_cero.append(num)
    return numeros_cero
numerillos=[4, 23,40, -7, 0, 14, 1000, -760]

#Ejercicio taller 2 VER
def cadenas_validas():
    resultado= ""
    while True:
        entrada=input("Cadena: ")
        if len(entrada)==0:
            break
        resultado+= entrada
    return resultado.split(" ")
#print(cadenas_validas())


#Ejercicio taller 3
def rotaciones_palabra(palabra):
    rotaciones=[]
    for i in range(len(palabra)):
        rotada=palabra[i:]+palabra[:i]
        rotaciones.append(rotada)
    return rotaciones

#Ejercicio taller 4
def main1():
    numeros=[]
    for n in range(16):
        num=input("Ingrese un número: ")
        while not num.isdigit():
            num=input("Ingrese un numero: ")
        numeros.append(num)
    contador=0
    for numero in numeros:
        print(numero, end=" ")
        contador += 1
        if contador%4==0:  
            print("")  

        
#Ejercicio taller 4
def elementos_iguales(sec1,sec2):
    lista_elementos=[]
    contador_elementos=0
    for i in sec1:
        if sec1[contador_elementos] in sec2:
            if sec1[contador_elementos] in lista_elementos:
                contador_elementos+=1
            else:
                lista_elementos.append(sec1[contador_elementos])
                contador_elementos+=1
        else: 
            continue
    return lista_elementos

#Ejercicio taller 5
def elementos_y_secuencias(A,B):
    contador_elementos=0
    contador_elementos_estan=0
    for i in A:
        if A[contador_elementos] in B:
            contador_elementos_estan+=1
            contador_elementos+=1
        else:
            continue
    if contador_elementos_estan==len(A):
        return True
    return False

#Ejercicio taller 6
def miki_moko():
    for i in range(1,101):
        if i%5==0 and i%3==0:
            print("MikiMoko")
        elif i%5==0 and i%3!=0:
            print("Moko")
        elif i%3==0 and i%5!=0:
            print("Miki")
        else:
            print(i)

#Ejercicio taller 7
def maximos_de_columnas(lista):
    lista_nueva=[]
    lista_maximos=[]
    for i in range(len(lista[0])):
        columna=[]
        for j in range(len(lista)):
            columna.append(lista[j][i])
        lista_nueva.append(columna)
    for listas in lista_nueva:
        maximo=max(listas)
        lista_maximos.append(maximo)
    return lista_maximos

listaxd=[[1, -2, 8, 4], 
         [6, -7, 3, 3],
         [6, -5, 4, 9]]

#Continuacion ejercicios parcial de la pagina
def obtener_slogan(palabra,n):
    nueva_cadena=""
    palabra_cortada=""
    palabra_cortada=palabra[0]+palabra[1]
    nueva_cadena=(palabra_cortada+","+" ")*n+palabra+" "+palabra[0]+(palabra[1]*(n+1))
    return nueva_cadena


def mejor_version(version1,version2):
    version1lista=version1.split(".")
    version2lista=version2.split(".")
    if int(version1lista[0])>int(version1lista[0]):
        return 1
    elif int(version1lista[0])<int(version2lista[0]):
        return -1
    elif int(version1lista[0])==int(version2lista[0]):
        if int(version1lista[1])>int(version2lista[1]):
            return 1
        elif int(version1lista[1])<int(version2lista[1]):
            return -1
        elif int(version1lista[1])==int(version2lista[1]):
            if int(version1lista[2])>int(version2lista[2]):
                return 1
            elif int(version1lista[2])<int(version2lista[2]):
                return -1
            else:
                return 0

def cadena_sin_repetir(cadena):
    cadena_nueva=""
    for l in range(len(cadena)):
        if l==0 or cadena[l]!=cadena[l-1]:
            cadena_nueva+=cadena[l]
    return cadena_nueva

def tupla_de_numeros(A,B):
    lista_nueva=[]
    for i in range (len(A)):
        numero_A=A[i]
        numero_B=B[i]
        lista_nueva.append((numero_A,numero_B))
    return lista_nueva

def main2():
    def verificar():
        while True:
            numero=input("Ingrese un número: ")
            if not numero.isdigit():
                continue
            else:
                return numero
    a=verificar()
    b=verificar()
    for i in range(int(a)):
        if i%int(b)==0:
            print(i)

def es_frase_palindromo(frase):
    frase_nueva=(frase.lower()).replace(" ","")
    frase_al_reves=""
    for i in range(len(frase_nueva)-1,-1,-1):
        frase_al_reves+=frase_nueva[i]
    if frase_nueva==frase_al_reves:
        return True
    return False

def traductor_latin_cerdos(oracion):
    lista_oracion=oracion.split()
    oracion_nueva=[]
    letra_a_cambiar=[]
    oracion_final=[]
    for i in range(len(lista_oracion)):
        letra_a_cambiar=lista_oracion[i][0]
        oracion_nueva=lista_oracion[i][1:len(lista_oracion[i])]+letra_a_cambiar+"ay"
        oracion_final.append(oracion_nueva)
    oracion_final=" ".join(oracion_final)
    return oracion_final

def validar_verificador(numero):
    suma=0
    lista_numeros=numero.split("-")
    for n in range(len(lista_numeros[0])):
        suma+=int(lista_numeros[0][n])
    resultado=suma%10
    if resultado==int(lista_numeros[1]):
        return "Válido"
    return "Inválido"

def main3():
    cadena_nueva=""
    while True:
        letra=input("Ingrese una letra: ")
        if  letra.isdigit():
            continue
        elif len(letra)>1:
            continue
        elif letra =="":
            break
        else:
            cadena_nueva+=letra
    print("".join(sorted(cadena_nueva)))

def palindromo(cadena):
    cadena_lista=cadena.split()
    contador_palabras=0
    for i in range(len(cadena_lista)):
        if cadena_lista[i]==cadena_lista[i][::-1]:
            contador_palabras+=1
    return contador_palabras

def palabras_invertidas(cadena):
    lista_palabras=cadena.split()
    lista_invertidas=[]
    cadena_nueva=""
    for palabras in lista_palabras:
        lista_invertidas.append(palabras[::-1])
    cadena_nueva=" ".join(lista_invertidas)
    return cadena_nueva

def tablero_ajedrez(n):
    total_numeros=n*n
    contador=0
    for i in range(total_numeros):
        if i%2!=0:
            print("n", end=" ")
            contador+=1
        else:
            print("b", end=" ")
            contador+=1
        if contador%n==0:
            print()

def main4():
    def validar_cadena():
        
        while True: 
            cadena=input("ingrese una frase: ")
            contador=0
            for l in cadena:
                if not l.isspace() and not l.isalpha():
                    contador+=1
            if contador>0:
                continue
            return cadena
    frase=validar_cadena()
    def validar_letra():
        while True:
            l=input("Ingrese una letra: ")
            if not l.isalpha():
                continue
            return l
    letra=validar_letra()
    contador_palabras=0
    lista_palbras=frase.split()
    for palabra in lista_palbras:
        if palabra[0]==letra or palabra[-1]==letra:
            contador_palabras+=1
    return contador_palabras

def main5():
    def verificar_cadena():
        while True:
            cadena=input("Ingrese una cadena: ")
            if cadena=="":
                continue
            return cadena
    cadena=verificar_cadena()
    def verificar_numero():
        while True:
            n=input("Ingrese un numero: ")
            if not n.isdigit():
                continue
            return n
    numero=verificar_numero()
    cadena_nueva=""
    contador=0
    for l in cadena:
        cadena_nueva+=l
        contador+=1
        if contador%int(numero)==0:
            cadena_nueva+="-"
    print(cadena_nueva)

def sacudir_matriz(matriz):
    for n in range(len(matriz)):
        if n%2==0:
            numero=matriz[n].pop()
            matriz[n].insert(0,numero)
        else:
            numero2=matriz[n].pop(0)
            matriz[n].insert(len(matriz[n])-1,numero2)
    return matriz

def lista_divisores(lista,n):
    lista_divisores=[]
    if n<0:
        return lista_divisores
    else:
        for num in lista:
            if n%num==0:
                lista_divisores.append(num)
        return lista_divisores

import math
def main6():
    def validar_angulo():
        while True:
            numero=input("Ingrese un número: ")
            if not numero.isdigit():
                continue
            if int(numero)>360 or int(numero)<0:
                continue
            return numero
    angulo=validar_angulo()
    angulo_radianes=(int(angulo)*math.pi)/180
    print(angulo_radianes)

def palabras_misma_letra(cadena):
    contador_palabras=0
    lista_palabras=cadena.split()
    for i in range(len(lista_palabras)):
        if (lista_palabras[i][0].lower())==(lista_palabras[i][-1].lower()):
            contador_palabras+=1
    return contador_palabras

def extension_admitida(ruta,extensiones):
    lista_ruta=ruta.split(".")
    if lista_ruta[1] not in extensiones:
        return False
    return True

def matriz_traspuesta(matriz):
    matriz_nueva=[]
    for i in range(len(matriz[0])):
        fila_nueva=[]
        for j in range(len(matriz)):
            elemento_nuevo=matriz[j][i]
            fila_nueva.append(elemento_nuevo)
        matriz_nueva.append(fila_nueva)
    return matriz_nueva

def nombres():
    contador=1
    nombres=""
    while contador<7:
        nombre=input(f"Ingrese el {contador} nombre: ")
        if not nombre.isalpha():
            continue
        if contador==6:
            nombres+=nombre
            contador+=1
        else:
            nombres+=nombre+","
            contador+=1
    lista_nombres=nombres.split(",")
    lista_nombres.sort()
    for i in range (len(lista_nombres)):
        inicial=lista_nombres[i][0]
        lista_nombres[i]=inicial.upper()+lista_nombres[i][1:len(lista_nombres[i])]
    frase_nueva=",".join(lista_nombres)
    return frase_nueva

def cambiar_cadena(cadena):
    cadena_nueva=""
    inicial=cadena[0]
    for l in cadena:
        if l==inicial.lower() or l==inicial.upper():
            cadena_nueva+="*"
        else:
            cadena_nueva+=l
    return cadena_nueva

def snake_a_camel(cadena):
    lista_cadena=cadena.split("_")
    palabra_modif=""
    for p in range(len(lista_cadena)):
        inicial=lista_cadena[p][0]
        lista_cadena[p] = inicial.upper()+lista_cadena[p][1:len(lista_cadena[p])]
        print(palabra_modif)
    lista_cadena="".join(lista_cadena)
    return lista_cadena

