class Caja:
    def __init__(self,billetes):
        denominaciones=[1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
        self.caja=billetes
        for key in self.caja:
            if key not in denominaciones:
                raise ValueError(f"Denominación {key} no permitida")
    def __str__(self):
        total=0
        for key in self.caja:
            monto_segun_billete=self.caja[key]*key
            total+=monto_segun_billete
        self.total=total
        print(f"Caja={self.caja} total={self.total} pesos")
        return ""
    def agregar(self,billetes):
        denominaciones=[1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
        for key in billetes:
            if key in self.caja:
                self.caja[key]+=billetes[key]
                self.total+=(billetes[key]*key)
            elif key not in self.caja and key in denominaciones:
                self.caja[key]=billetes[key]
                self.caja = dict(sorted(self.caja.items(), key=lambda x: x[0], reverse=True))
                self.total+=(billetes[key]*key)
            else:
                raise ValueError(f"Denominación {key} no permitida")
    def quitar(self,billetes):
        total_sacado=0
        for key in billetes:
            if billetes[key]>self.caja[key]:
                raise ValueError(f"No hay suficientes billetes de denominacion {key}")
            self.caja[key]-=billetes[key]
            if self.caja[key]==0:
                self.caja.pop(key,None)
            self.total-=(billetes[key]*key)
            total_sacado+=(billetes[key]*key)
        print(total_sacado)
            
c=Caja({500: 6, 100: 7, 2: 4})
str(c)
c.agregar({50:2, 2:1})
str(c)
c.quitar({50:2,100:1})
str(c)