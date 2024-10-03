def disponibilidad_para_juntarse(dicc):
    lista_dias=[]
    lista_parcial=[]
    dias_semana=["LUN", "MAR", "MIE","JUE","VIE","SAB","DOM"]
    for key in dicc:
        for dia in dicc[key]:
            lista_parcial.append(dia)
    contador=0
    for d in dias_semana:
        for dias in lista_parcial:
            if d==dias:
                contador+=1
        if contador==len(dicc):
            lista_dias.append(d)
        contador=0
    return lista_dias
diccionario={ 'Juan': ['MIE', 'VIE', 'SAB'], 'Jose': ['VIE', 'SAB', 'DOM'], 'Jorge': ['JUE', 'VIE', 'SAB'] }

def palabras_segun_personas(ruta):
    dicc={}
    dicc_palabras={}
    with open(ruta,"r") as archivo:
        for linea in archivo:
            linea=linea.strip()
            persona,frase=linea.split(":")
            if persona not in dicc:
                dicc[persona]=""
            palabras=frase.split()
            for palabra in palabras:
                if palabra not in dicc_palabras:
                    dicc_palabras[palabra]=0
                dicc_palabras[palabra]+=1
            dicc[persona]=dicc_palabras
            dicc_palabras={}
    return dicc

class Vaca:
    def __init__(self):
        pass
    def sorondear(self):
        return "Muuuu!"
    
vaca=Vaca()
vaca.sorondear()

class Ovni:
    def __init__(self,nave):
        self.nave=nave
        self.objeto=""
    def __str__(self):
        if self.objeto!="":
            return f"Nave {self.nave} (estación de sondeo ocupada)"
        return f"Nave {self.nave} (estación de sondeo vacia)"
    def abducir(self,objeto):
        if self.objeto!="":
            raise ValueError
        self.objeto=objeto
    def sorondear(self):
        if self.objeto=="":
            raise ValueError
        sondeo=self.objeto.sorondear()
        print(f"sorondeando...{sondeo}...ups el sujeto exploto")
        self.objeto=""

dicc={"Juan": "27/05/1993", "Alicia": "30/11/1990", "Elena": "27/05/1985"}
def mismo_cumpleaños(dicc):
    nuevo_dicc={}
    for keys in dicc:
        dia,mes,año=dicc[keys].split("/")
        dia_y_mes=dia+"/"+mes
        if dia_y_mes not in nuevo_dicc:
            nuevo_dicc[dia_y_mes]=[]
            nuevo_dicc[dia_y_mes].append(keys)
        else:
            nuevo_dicc[dia_y_mes].append(keys)
    return nuevo_dicc

def resumen_pedidos(lista,ruta):
    dicc_total={}
    for pedidos in lista:
        for elementos in pedidos:
            if elementos not in dicc_total:
                dicc_total[elementos]=0
                dicc_total[elementos]+=pedidos[elementos]
            else:
                dicc_total[elementos]+=pedidos[elementos]
    print(dicc_total)
    with open(ruta,"w") as archivo_destino:
        for producto,cantidad in dicc_total.items():
            linea_a_escribir=producto+";"+str(cantidad)
            archivo_destino.write(linea_a_escribir+"\n")
pedidos = [
    {"manzanas": 5, "bananas": 3},
    {"manzanas": 2, "peras": 4},
    {"bananas": 2, "naranjas": 6}
]


class Materia():
    def __init__(self,nombre,creditos,descripcion):
        self.nombre=nombre
        self.creditos=creditos
        self.nota=0
        self.correlativas=[]
        self.desctripcion=descripcion
    def imprimir_informacion(self):
        print(f"Nombre de la materia: {self.nombre}")
        print(f"Descripcion: {self.desctripcion}")
        print(f"Créditos: {self.creditos}")
        if self.esta_aprobada()==True:
            print("Aprobada")
        else:
            print("No aprobada")
    def esta_aprobada(self):
        if self.nota<4:
            return False
        return True
    def asignar_nota(self,nota):
        if nota<0 or nota>10:
            raise ValueError
        self.nota=nota
    def agregar_correlativa(self,correlativa):
        self.correlativas.append(correlativa)
    def puede_cursarse(self):
        for materias in self.correlativas:
            if materias.esta_aprobada()==False:
                return False
            return True

def cadena_segun_longitud(cadena):
    res={}
    cadena_lista=cadena.split()
    for palabra in cadena_lista:
        longitud=len(palabra)
        if longitud not in res:
            res[longitud]=[]
            res[longitud].append(palabra)
        else:
            res[longitud].append(palabra)
    return res

def peso_gundam(ruta,nombre):
    with open(ruta,"r") as archivo:
        for linea in archivo:
            linea=linea.strip()
            gundam,parte,peso=linea.split(",")
            if gundam==nombre:
                return peso

class Cuenta:
    def __init__(self,apellido):
        self.apellido=apellido
        self.monto=0
        self.movi=[]
    def acreditar(self,monto,ocasion):
        self.monto+=monto
        self.movi.append(("Acreditacion",monto,ocasion))
    def extraer(self,monto,ocasion):
        if monto>self.monto:
            raise ValueError("Fondos Insuficientes")
        self.monto-=monto
        self.movi.append(("extraccion",monto,ocasion))
    def saldo(self):
        print(self.monto)
    def __str__(self):
        return f"Cuenta de {self.apellido}"
    def transferir(self,monto,cuenta):
        cuenta.acreditar(monto,f"cuenta de {self.apellido}")
        self.extraer(monto,f"cuenta de {cuenta.apellido}")
    def movimientos(self):
        print(f"{self.movi}")

def traducir_a_ingles(cadena,dicc):
    lista_cadena=cadena.split()
    nueva_cadena=""
    for palabras in lista_cadena:
        if palabras in dicc:
            nueva_cadena+=dicc[palabras]+" "
        else:
            nueva_cadena+= palabras+" "
    return nueva_cadena
dicc={"hola":"hello", "bienvenido":"welcome"}

def notas_a_csv(ruta_origen,ruta_destino):
    promedio=0
    suma=0
    with open(ruta_origen,"r") as archivo_origen,open(ruta_destino,"w") as archivo_destino:
        for linea in archivo_origen:
            linea=linea.strip()
            lista_linea=linea.split(",")
            if len(lista_linea)>2:
                cant_notas=len(lista_linea[1:])
                for n in range(1,len(lista_linea)):
                    suma+=int(lista_linea[n])
                promedio=suma/int(cant_notas)
                linea_csv=lista_linea[0]+";"+str(promedio)
                archivo_destino.write(linea_csv+"\n")
                suma=0        
            else:
                linea_csv=lista_linea[0]+";"+str(lista_linea[1])
                archivo_destino.write(linea_csv+"\n")

class Partido:
    def __init__(self,local,visitante):
        self.local=local
        self.visitante=visitante
    def cargar_resultado(self,gol_local,gol_visitante):
        self.gol_local=gol_local
        self.gol_visitante=gol_visitante
    def obtener_ganador(self):
        if self.gol_local>self.gol_visitante:
            return self.local
        if self.gol_local<self.gol_visitante:
            return self.visitante
        if self.gol_local==self.gol_visitante:
            return None
    def obtener_perdedor(self):
        if self.gol_local<self.gol_visitante:
            return self.local
        if self.gol_local>self.gol_visitante:
            return self.visitante
        if self.gol_local==self.visitante:
            return None
class Liga:
    def cargar_partido(self,partido):
        self.equipos={}
        if partido.local not in self.equipos:
            self.equipos[partido.local]=0
        if partido.visitante not in self.equipos:
            self.equipos[partido.visitante]=0
        if partido.obtener_ganador()==partido.local:
            self.equipos[partido.local]+=3
        elif partido.obtener_ganador()==None:
            self.equipos[partido.local]+=1
            self.equipos[partido.visitante]+=1
        elif partido.obtener_ganador()==partido.visitante:
            self.equipos[partido.visitate]+=3
    def obtener_campeon(self):
        goles_max=0
        for keys in self.equipos:
            if self.equipos[keys]>goles_max:
                goles_max=self.equipos[keys]
                ganador=keys
        return ganador   

def archivo_cambiado(ruta):
    equipos={}
    with open(ruta,"r") as archivo:
        for linea in archivo:
            linea=linea.strip()
            equipo,jugador,fecha,goles=linea.split(",")
            if equipo not in equipos:
                equipos[equipo]=int(goles)
            else:
                equipos[equipo]+=int(goles)
            print(f"El jugador {jugador} hizo {goles} goles")
    for keys in equipos:
        print(f"El equipo {keys} hizo {equipos[keys]} goles")

class Semaforo:
    def __init__(self):
        self.roja=True
        self.amarilla=False
        self.verde=False
        self.ult_luz=""
    def siguiente(self):
        if self.roja==True:
            self.amarilla=True
            self.roja=False
        elif self.amarilla==True:
            self.verde=True
            self.amarilla=False
        elif self.verde==True:
            self.roja=True
            self.verde=False
        else:
            raise ValueError
    def apagar(self):
        if self.verde==True:
            self.ult_luz="Verde"
        elif self.amarilla==True:
            self.ult_luz="Amarilla"
        elif self.roja==True:
            self.ult_luz="Roja"
        self.roja=None
        self.amarilla=None
        self.verde=None
    def encender(self):
        if self.ult_luz=="Verde":
            self.roja=False
            self.amarilla=False
            self.verde=True
        elif self.ult_luz=="Amarilla":
            self.roja=False
            self.verde=False
            self.amarilla=True
        elif self.ult_luz=="Roja":
            self.amarilla=False
            self.verde=False
            self.roja=True
    def __str__(self):
        if self.roja==None:
            return "Semaforo apagado"
        elif self.roja==True:
            return f"Luz encendida: roja"
        elif self.amarilla==True:
            return f"Luz encendida: amarilla"
        elif self.verde==True:
            return f"Luz encendida: verde"

def regalos_segun_mes(cumpleanios,regalos,precios):
    res={}
    for key in cumpleanios:
        fecha=cumpleanios[key]
        dia,mes,anio=fecha.split("/")
        if mes not in res:
            res[mes]=0
        regalo=regalos[key]
        precio_regalos=precios[regalo]
        res[mes]+=float(precio_regalos)
    return res

def separar_curso(ruta):
    with open(ruta,"r") as archivo_csv,open("grupo1.txt","w") as archivo_grupo1,open("grupo2.txt","w") as archivo_grupo2:
        for linea in archivo_csv:
            linea=linea.strip()
            lista_linea=linea.split(",")
            if int(lista_linea[0])%2==0:
                archivo_grupo2.write(lista_linea[0]+"\n")
            else:
                archivo_grupo1.write(lista_linea[0]+"\n")
class Boleteria:
    def __init__(self,evento,localidades):
        self.evento=evento
        self.localidades=localidades
        self.vendidas=0
    def vender_localidades(self,cant_localidades):
        if (self.vendidas+cant_localidades)>self.localidades:
            raise ValueError("No hay localidades suficientes")
        self.vendidas+=cant_localidades
    def localidades_agotadas(self):
        if self.localidades==self.vendidas:
            print(True)
        else:
            print(False)
    def __str__(self):
        return f"Evento: {self.evento} - localidades vendidas: {self.vendidas} de {self.localidades}"

def palabra_mas_repetida(cadena):
    dicc_cantidad={}
    valor_max=0
    lista_cadena=cadena.split()
    for palabra in lista_cadena:
        if palabra not in dicc_cantidad:
            dicc_cantidad[palabra]=0
        dicc_cantidad[palabra]+=1
    for keys in dicc_cantidad:
        if dicc_cantidad[keys]>valor_max:
            valor_max=dicc_cantidad[keys]
            palabra_max=keys
    tupla=(palabra_max,valor_max)
    return tupla

def goles_y_equipos(ruta_csv):
    dicc_equipos={}
    with open(ruta_csv,"r") as archivo_csv:
        for linea in archivo_csv:
            linea=linea.strip()
            equipo,jugador,fecha,goles=linea.split(",")
            if equipo not in dicc_equipos:
                dicc_equipos[equipo]={}
            if jugador not in dicc_equipos[equipo]:
                dicc_equipos[equipo][jugador]=0
            dicc_equipos[equipo][jugador]+=int(goles)
    return dicc_equipos

class Tatuaje:
    def __init__(self,nombre,area,dolor):
        self.nombre=nombre
        self.area=area
        self.dolor=dolor
class Brazo:
    def __init__(self,area,aguante):
        self.area_brazo=area
        self.aguante_persona=aguante
class Tatuador:
    def __init__(self,nombre):
        self.tatuador=nombre
        self.tatuajes_hechos=0
    def tatuar(self,brazo_persona,tipo_tatuaje):
        if brazo_persona.aguante_persona<tipo_tatuaje.dolor:
            raise ValueError("No te lo vas a bancar")
        if brazo_persona.area_brazo<tipo_tatuaje.area:
            raise ValueError("Ya no te queda más lugar")
        brazo_persona.area_brazo-=tipo_tatuaje.area
        self.tatuajes_hechos+=1
    def __str__(self):
        return f"{self.tatuador}: {self.tatuajes_hechos} tatuajes realizados"

def frecuencia_palabras(cadena):
    res={}
    lista_cadena=cadena.split()
    for palabra in lista_cadena:
        if palabra not in res:
            res[palabra]=0
        res[palabra]+=1
    return res
dicc1=frecuencia_palabras("Esto es un  ejemplo de es cadena con palabras repetidas como ejemplo ejemplo")

def max_frecuencia(dicc):
    valor_max=0
    palabras_max=[]
    for keys in dicc:
        if dicc[keys]>=valor_max:
            valor_max=dicc[keys]
    for k in dicc:
        if dicc[k]==valor_max:
            palabras_max.append(k)
    palabras=",".join(palabras_max)
    return palabras

def cant_palabras(ruta):
    contador=1
    cant_palabras=0
    res={}
    with open(ruta,"r") as archivo:
        for linea in archivo:
            linea=linea.strip()
            lista_linea=linea.split()
            for palabras in lista_linea:
                cant_palabras+=1
            res[contador]=cant_palabras
            cant_palabras=0
            contador+=1
    return res
class App:
    def __init__(self,app,sist_op):
        self.apps=app
        self.sist=sist_op
class Smartphone:
    def __init__(self,nombre,sist_op):
        self.nombre=nombre
        self.sistema=sist_op
        self.apliaciones=[]
    def instalar(self,aplicacion):
        if aplicacion.apps in self.apliaciones:
            raise Exception("La app ya esta instalada")
        if self.sistema not in aplicacion.sist:
            raise Exception("La app no es compatible con el sistema operativo")
        self.apliaciones.append(aplicacion.apps)
    def __str__(self):
        apps=""
        for nombres in self.apliaciones:
            if nombres==self.apliaciones[len(self.apliaciones)-1]:
                apps+=nombres
            else:
                apps+=nombres+", "
        return f"{self.nombre} ({self.sistema}). Apps: {apps}"

def imprimir_notables(movimientos,N):
    dicc_mov={}
    for personaje,movimiento in movimientos:
        key=personaje+"-"+movimiento
        if key not in dicc_mov:
            dicc_mov[key]=0
        dicc_mov[key]+=1
    for k in dicc_mov:
        if dicc_mov[k]>N:
            print(f"{k} ({dicc_mov[k]})")

def separar_grupo(ruta):
    with open(ruta,"r") as archivo, open("grupo0.txt","w") as archivo_grupo0, open("grupo1.txt","w") as archivo_grupo1, open("grupo2.txt","w") as archivo_grupo2:
        for linea in archivo:
            linea=linea.strip()
            if int(linea)%3==2:
                archivo_grupo2.write(linea+"\n")
            elif int(linea)%3==1:
                archivo_grupo1.write(linea+"\n")
            elif int(linea)%3==0:
                archivo_grupo0.write(linea+"\n")

class CalendarioMes:
    def __init__(self,num):
        if num<28 or num>31:
            raise ValueError
        self.numero=num
        self.calendario={}
    def agregar_evento(self,dia,evento):
        if dia<1 or dia>self.numero:
            raise Exception
        if dia not in self.calendario:
            self.calendario[dia]=[]
        self.calendario[dia].append(evento)
    def eliminar_evento(self,dia,evento):
        if dia not in self.calendario or evento not in self.calendario[dia]:
            raise Exception
        if len(self.calendario[dia])>1:
            self.calendario[dia].remove(evento)
        elif len(self.calendario[dia])==1:
            self.calendario.pop(dia)
    def obtener_eventos(self,dia):
        if dia>self.numero or dia<1:
            raise Exception
        if dia not in self.calendario:
            return []
        else:
            return self.calendario[dia]
        
def juntada_amigos(dicc):
    res={}
    for n in range(1,32):
        res[n]=[]
    for keys in dicc:
        lista_media=dicc[keys]
        for k in res:
            if k not in lista_media:
                res[k].append(keys)
    return res
disponibilidad = {
    'Alice': [1, 2, 5, 10, 15],
    'Bob': [3, 4, 7, 10, 20],
    'Charlie': [1, 6, 9, 12, 25],
    'David': [2, 8, 15, 18, 22],
    'Eve': [5, 11, 13, 19, 24]
}
