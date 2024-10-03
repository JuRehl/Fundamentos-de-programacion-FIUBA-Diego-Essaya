def pedir_entero(min,max,msj):
    while True:
        entrada= input(msj, "[" + str(min) + ";" + str(max) +"]" )
        if not entrada.isdigit():
            continue
        numero=int(entrada)
        if not (min <= numero <= max):
            continue
        if not entrada == int:
            continue
        return numero    
pedir_entero(-50, 50,"Cual")

#Version con try y except
def pedir_entero_clase(min,max,msj):
    while True:
        entrada= input(msj, "[" + str(min) + ";" + str(max) +"]" )
        try:
            n=int(entrada)
        except ValueError: #como agregar excepciones except (ValueError, TypeError) o agregar otra linea de except
            print("No ingresaste un entero")
            continue
        if not (min <= n <= max):
            print("El rango es inválido")
            continue
        return n
    