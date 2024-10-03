def main():
    #
    pesosinicial=int(input("Ingrese una cantidad de pesos: "))
    interes= int(input("Ingrese la tasa de interés: "))
    años=int(input("Ingrese la cantidad de años: "))
    def monto_final(pesosinicial, interes, años):
        #le doy una cantidad inicial de pesos, interes y años y te muestra cuanto obtenes
        adentro_pot=1+(interes/100)
        ecuacion=pesosinicial * adentro_pot
        return(ecuacion)
    print(monto_final(pesosinicial,interes,años))
main()