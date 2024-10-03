class Fraccion:
    def __init__(self,dividendo,divisor):
        self.dividendo=dividendo
        self.divisor=divisor
        if self.divisor==0:
            raise ZeroDivisionError("No se puede dividir por cero")
    def __str__(self):
        print(f"{self.dividendo}/{self.divisor}")
    def __add__(self,otra):
        divisor=self.divisor*otra.divisor
        dividendo1=divisor*self.dividendo
        dividendo2=divisor*otra.dividendo
        dividendo=dividendo1+dividendo2
        return self.__init__(dividendo,divisor)
    def __mul__(self,otra):
        dividendo=self.dividendo*otra.dividendo
        divisor=self.divisor*otra.divisor
        return self.__init__(dividendo,divisor)
    
