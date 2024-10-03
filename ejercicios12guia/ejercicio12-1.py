#Ejercicio 12.1  a,b,c,d
class Intervalo:
    def __init__(self,desde,hasta):
        self.desde=desde
        self.hasta=hasta
        if self.desde>self.hasta:
            print("Desde, debe ser menor de hasta")
    def duracion(self):
        duracion=self.hasta-self.desde
        return duracion
    def interseccion(self, otro):
        inicio=max(self.desde, otro.desde)
        fin=min(self.hasta,otro.hasta)
        if inicio<fin:
            return inicio,fin
        raise ValueError ("No hay interseccion entre los intervalos")
    def union(self,otro):
        if not (self.hasta==otro.hasta or self.desde==otro.desde) and self.interseccion(otro)==ValueError:
            raise ValueError("Los intervalos no son adyacentes ni se intersecan")
        else:
            return(self.interseccion(otro.desde,otro.hasta))

clase1=Intervalo(10,20)
clase2=Intervalo(40,50)
union=clase1.union(clase2)