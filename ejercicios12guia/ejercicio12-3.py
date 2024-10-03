#Ejercicio 12.3
class Vector:
    def __init__(self,coords):
        self.coords=coords
    def __str__(self):
        print(f"{self.coords}")
    def __add__(self,otro):
        res=[]
        if len(self.coords)==len(otro.coords):
            for c in range(len(self.coords)):
                num=self.coords[c]+otro.coords[c]
                res.append(num)
            return res
        raise ValueError("Las dimensiones de los vectores son distintas")
    def __mul__(self,N):
        res=[]
        for numero in self.coords:
            num_mult=numero*N
            res.append(num_mult)
        return res
    