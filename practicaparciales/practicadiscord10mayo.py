#ejercicio 2
def usuario_que_mas_dono(lista):
    dicc={}
    for usuario,donacion in lista:
        if not usuario in dicc:
            dicc[usuario]=0
        dicc[usuario]+=donacion
    donacion_max=-1
    usuario_max=[]
    for usuario in dicc.keys():
        if donacion_max<dicc[usuario]:
            usuario_max=usuario
            donacion_max=dicc[usuario]
        elif donacion_max==dicc[usuario]:
            usuario_max.append(usuario)
    donantes=",".join(usuario_max)
    print(f"Maximos donantes {donantes}")
 
#Ejercicio 1
def empleados_por_proyecto(ruta_origen,ruta_destino):
    dicc={}
    with open(ruta_origen,"r") as origen,open(ruta_destino,"w") as destino:
        for linea in origen:
            nombre,proyecto=linea.strip().split(",")
            if proyecto not in dicc:  #dicc.get(proy,[])
                dicc[proyecto]=[]
            dicc.apend(nombre)
        for proyecto in dicc:
            destino.write(proyecto +"-->"+",".join(dicc[proyecto])+"\n")

#Ejercicio 3
class Materia:
    def __init__(self,nombre,desc,cont_cred):
        self.name=nombre
        self.desc=desc
        self.cred=cont_cred
        self.nota=0
        self.corr=[]
    def asignar_nota(self,nota):
        if nota<0 or nota>10:
            raise ValueError
        self.nota=nota
    def esta_aprobada(self):
        return self.nota>=4
    def agregar_correlativa(self,corr):
        self.corr.append(corr)
    def puede_cursarse(self):
        for materia in self.corr:
            if not materia.esta_aprobada():
                False
            return True
    def imprimir_info(self):
        print(self.name)
        print(self.desc)
        print(self.cred)
        if self.esta_aprobada():
            print("Esta aprobado")
        else:
            print("Esta desaprobado")
            
