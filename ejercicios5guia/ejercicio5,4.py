#Ejercicio 5.4 
import random
def main():
    """Genera un numero random y el usuario debe adivinarlo"""
    numero= random.randrange(1,100)
    numero_usuario= 0
    while numero_usuario>=0 and numero_usuario<=100:
        numero_usuario=int(input("Adivine un numero del 1 al 100: "))
        if numero_usuario<numero:
            print("EL número es mayor")
        elif numero_usuario>numero:
            print("El numero es menor")
        else:
            print("Felicidades es el numero correcto")
            numero_usuario=200
main()
        
