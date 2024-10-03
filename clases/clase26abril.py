"""Diccionarios (casi instantánea)--> calve:valor NO TIENEN ORDEN
La clave es inmutable y no se pueden repetir
En get si le doy una clave que existe y un valor no te da el valor que le das sino el ya existente
en cambiosi le doy una clave que no existe y el valor si me devuelve el valor escrito"""
#Ejercicio 9.2 otra resolucion
def contar_palabras(texto):
    palabras=texto.split()
    dicc={}
    for palabra in palabras: #otra forma dicc[palabra]=dicc.get(palabra,0)+1
        if not palabra in dicc:
            dicc[palabra]=0
        dicc[palabra]+=1
    return dicc

#Ejercicio 9.1
def tuplas_a_diccionario(tuplas):
    res={}
    for clave,valor in tuplas:
        if clave not in res: #alternativa get --> res[clave]=res.get(clave,[]) sig instruccion--> res[clave].append(valor)
            res[clave]=[]
        res[clave].append(valor)
    return res

"""set() diccionario que solo tiene claves, solo valores inmutable NO respetidos"""
def union(l1,l2):
    res=set()
    for e in l1:
        res.add(e) #si ya esta, no lo vuelve a agregar ya que no se pueden repetir valores, add funcion especial del set
    for e in l2:
        res.add(e)
    return list(res)

#Ejercicio 9.4
def palabra_mas_larga(cadena):
    res={}
    for palabra in cadena.split():
        for c in palabra:
            if not c in res:
                res[c]=palabra 
            if len(res[c])<len(palabra):
                res[c]=palabra
    return res

"""Objetos --> Los objetos son instancias de la clase
los objetos son mutables"""
#Ejercicio 12.2
class fraccion:
    def __init__(self, num, den):
        if den==0:
            raise ZeroDivisionError #como que "levanta" un error
        self.num=num #-->son propios del objeto que creamos (se pueden llamar atributos)
        self.den=den
        self.simplificar()
    def sumar(self,otra):
        num=self.num*otra.den+self.den*otra.num
        den=self.den*otra.den
        return fraccion(num,den)
    #def simplificar(self):
        #aca suponemos que tenemos una funcion para el mcd en otro archivo
        #divisor=gcd(self.num,self.den)
        #self.num=self.num/divisor
        #self.den=self.div/divisor
        #Aunque no devuelva nada hace la modificacion de simplificar
    def __str__(self): #metodo str -->ver que hace si no esta escrita la funcion y lo imprimimos
        """Convierte el parámetro en cadena"""
        return f"{self.num}/{self.den}"
    def __add__(self,otra):
        return self.sumar(otra)
    
#Ejercicio 12.3
class vector:
    def __init__(self,coords):
        self.coords
    def __add__(self,otra):
        res=[]
        for i in range(len(self.coords)):
            res.append(self.coords[i]+otra.coords[i])
        return vector(res) #aca devolves el objeto vector, una nueva instancia del objeto vector

#metodos para entender mejor
class Punto:
    def __init__(self,x,y):
        self.x=x
        self.y=y
#Los atributos de un objeto pueden ser cualquier cosa
class Rectangulo:
    def __init__(self,p1,p2):
        self.p1=p2
        self.p2=p2
    def area(self):
        b=abs(self.p1.x-self.p2.x) #-->se denomina composicion de objetos
        h=abs(self.p1.y-self.p2.y)
        return b*h
"""si hago p1.x=0 se cambia el objeto ya que SON MUTABLES
Si modifico el punto y el rectangulo no crea uno nuevo se cambia el punto en sí"""
