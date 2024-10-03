import random

#Ejemplo parcial 1 (ejercicio 7.11 parecido)
texto="Hola che como va hoy?"
def plegar(texto, N):
    parrafo=[]
    linea=[]
    longitud_linea=0
    for palabra in texto.split():
        if N<longitud_linea+len(palabra):
            parrafo.append(" ".join(linea))
            linea=[]
            longitud_linea=0
        linea.append(palabra)
        longitud_linea+=len(palabra)+1
    parrafo.append(" ".join(linea))
    return parrafo
#print(plegar(texto,8))

#Ejercicio Discord 2
def pedir_resultados():
    while True:
        resultado_partido=input("Ingrese un valor de resultado de un partido de la forma <pais>:<pais>-<goles>:<goles>: ")
        dividir_resultado=resultado_partido.split("-")
        if len(dividir_resultado)!=2:
            continue
        paises,goles=dividir_resultado
        paises=paises.split(":")
        goles=goles.split(":")
        if len(goles)!=2 or len(paises)!=2:
            continue
        pais1,pais2=paises
        goles1,goles2=goles
        if not goles1.isdigit() or not goles2.isdigit():
            continue
        return pais1,pais2,int(goles1),int(goles2)
#print(pedir_resultados())

#Ejercicio Discord 1
def calcular_traza(m):
    suma=0
    for i in range(len(m)):
        suma+=[i][i]
    return suma

def filtrar_ms(lista,n):
    res=[]
    for m in lista:
        if calcular_traza(m)>=1:
            res.append(m)
    return res


#Ejercicio Discord 3
def main():
    print("Tirando dado...")
    numero=random.randint(1,6)
    n_tiradas=1
    anterior=0
    while numero!=anterior and n_tiradas%6!=numero:
        print("tirando dado...")
        anterior=numero
        numero=random.randint(1,6)
        n_tiradas+=1
    print(f"tardo {n_tiradas}")
main()
