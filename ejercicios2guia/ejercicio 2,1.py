def monto_final(pesosinicial, interes, años):
    #le doy una cantidad inicial de pesos, interes y años y te muestra cuanto obtenes
    adentro_pot=1+(interes/100)
    ecuacion=pesosinicial * adentro_pot
    return(ecuacion)
print(monto_final(50,25,20))