import os
CARACTERES_COMUNES=[",",".","!",";","?"]
SALIDA="e"

def verificar_ruta():
    """Función para verificar la ruta que me ingresa el usuario. En el caso que sea una ruta válida, la devuelve"""
    while True:
        ruta=input("Ingrese la ruta del directorio donde se realizara el anális o e para salir ")
        if ruta==SALIDA:
            print("Saliendo del programa...")
            return SALIDA
        try:
            os.listdir(ruta)
        except NotADirectoryError:
            print("El directorio no fue encontrado")
            continue
        except FileNotFoundError:
            print("El archivo no fue encontrado")
            continue
        return ruta

def verificar_N():
    """Verifica el número a usar en los N-gramas"""
    while True:
        N=input("Ingrese un N entero entre 2 y 9 para realizar los N-gramas: ")
        try:
            int(N)  
        except ValueError:
            print("Debe ingresar un entero")
            continue
        N=int(N)
        if N<2 or N>9:
            print("El numero debe estar entre 2 y 9")
            continue
        return N
        
def limpiar_linea(linea):
    """Deja una linea de texto sin mayúsculas y caracteres que no estén dentro de los caracteres comúnes.
    Esto sirve a la hora de realizar los N-gramas y compararlos"""
    linea_nueva=[]
    palabra_nueva=""
    linea=linea.strip()
    linea=linea.lower()
    lista_linea=linea.split()
    for palabra in lista_linea:
            for caracter in palabra:
                if caracter in CARACTERES_COMUNES:
                    continue
                palabra_nueva+=caracter
            linea_nueva.append(palabra_nueva)
            palabra_nueva=""
    return linea_nueva

def hacer_N_gramas(numero,ruta_archivo):
    """Realiza el N-grama de un archivo"""
    dicc_n_gramas={}
    lista_n_gramas=[]
    try:
        with open(ruta_archivo,"r") as archivo:
            for linea in archivo:
                lista_linea=limpiar_linea(linea)
                for palabras in lista_linea:
                    lista_n_gramas.append(palabras)
                    if len(lista_n_gramas)==numero:
                        key=tuple(lista_n_gramas)
                        if key not in dicc_n_gramas:
                            dicc_n_gramas[key]=0
                        dicc_n_gramas[key]+=1
                        lista_n_gramas.pop(0)
                    elif len(lista_n_gramas)<numero:
                        continue
        return dicc_n_gramas
    except FileNotFoundError:
        return dicc_n_gramas

def similaridad(dicc1,dicc2):
    """Busca similaridad entre N-gramas, devuelve el porcentaje de esta"""
    A=0
    for keys in dicc1:
        A+=dicc1[keys]
    B=0
    for key in dicc2:
        B+=dicc2[key]
    A_y_B=0
    for keys in dicc1:
        if keys in dicc2:
            A_y_B+=(dicc1[keys]+dicc2[keys])
    try:
        jaccard_A_y_b=A_y_B/(A+B)
    except ZeroDivisionError:
        return float(0.00)
    if dicc1=={} or dicc2=={}:
        return float(0.00) 
    porcentaje=jaccard_A_y_b*100
    porcentaje=str(porcentaje)[:5]
    return float(porcentaje)

def comparar_archivos(archivos,N):
    """Compara los archivos, me devuelve un diccionario donde las keys son los archivos
    y los valores de estas es el porcentaje de similaridad"""
    dicc_resultados={}
    for a in range(len(archivos)):
        N_grama=hacer_N_gramas(N,archivos[a])
        for ar in range(a+1,len(archivos)):
            N_grama2=hacer_N_gramas(N,archivos[ar])
            key=(archivos[a],archivos[ar])
            dicc_resultados[key]=similaridad(N_grama,N_grama2)
    return dicc_resultados

def limpiar_claves(dicc_resultados):
    """Funcion que sirve para limpiar el diccionario ya que se tenia un diccionario con las keys 
    ("dir1/ejemplo1.txt","dir1/ejemplo2.txt") y me lo transforma a ("ejemplo1.txt","ejemplo2.txt") para facilitar
    a la hora de mostrarlo por pantalla y guardarlo en el archivo"""
    dicc_nuevo={}
    for clave,valor in dicc_resultados.items():
        clave1=clave[0].rsplit('/', 1)
        clave2=clave[1].rsplit('/', 1)
        clave_limpia=(clave1[1], clave2[1])
        dicc_nuevo[clave_limpia]=valor
    return dicc_nuevo
