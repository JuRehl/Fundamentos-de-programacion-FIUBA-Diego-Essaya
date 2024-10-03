import sixteen

def verificar_alto_ancho():
        while True:
            """Valido la entrada de el alto del tablero segun las precondiciones indicadas en el archivo sixteen.py"""
            alto_ancho=input("Ingrese el alto de su tablero, luego el ancho: ")
            if not alto_ancho.isdigit():
                continue
            valor_alto_ancho=int(alto_ancho)
            if not(valor_alto_ancho>1 and valor_alto_ancho<10):
                print("Ingrese un alto o ancho entre el 2 y 9")
                continue
            else:
                return valor_alto_ancho
            
def mostrar_tablero(tablero,alto,ancho):
        """Muestra el tablero, por terminal, ordenado para la vista del usuario"""
        print("   ", 0 , end= " | ")
        for num in range(1,ancho):
            print( num, end=" | ")
        print()
        print()
        numeros_alto=[]
        for num in range(alto):
            numeros_alto.append(num)
        contador_alto=0
        for filas in tablero:
            print(numeros_alto[contador_alto], end=" | ")
            contador_alto+=1
            for numero in filas:
                justificacion=str(numero).rjust(2," ")
                print(justificacion, end="| ")
            print()

def verificar_direcciones(alto,ancho):
        """Verifico si el usuario me da las direcciones como quiero"""
        while True:
            print("Direcciones: d (rotar hacia la derecha), i (rotar hacia la izquierda), a (rotar hacia arriba) b (rotar hacia abajo)")
            movimiento=input("Ingrese una fila o columna y una rotacion <direccion,num>, e para salir: ")
            if movimiento=="e":
                return movimiento
            elif "," not in movimiento:
                print("Ingrese el movimiento como se lo indica")
                continue
            if not movimiento[2].isdigit():
                continue
            if movimiento[0].isdigit():
                continue
            if len(movimiento)>3:
                continue
            if int(movimiento[2])>alto or int(movimiento[2])<0:
                continue
            if int(movimiento[2])>ancho or int(movimiento[2])<0:
                continue
            else:
                return movimiento

def realizar_movimientos(tablero,direccion,numero):
        """Funcion que realiza los movimientos segun la opcion elegida"""
        if direccion.lower()=="d":
            sixteen.rotar_derecha(tablero,int(numero))
        elif direccion.lower()=="i":
            sixteen.rotar_izquierda(tablero,int(numero))
        elif direccion.lower()=="a":
            sixteen.rotar_arriba(tablero,int(numero))
        if direccion.lower()=="b":
            sixteen.rotar_abajo(tablero,int(numero))

def main():
    """PROGRAMA PARA JUGAR AL JUEGO SIXTEEN"""
    
    alto_tablero=verificar_alto_ancho()
    ancho_tablero=verificar_alto_ancho()
    
    tablero_usuario=sixteen.crear_tablero(alto_tablero,ancho_tablero)
    sixteen.mezclar_tablero(tablero_usuario)

    print("Comienza el juego...") 
    mostrar_tablero(tablero_usuario,alto_tablero,ancho_tablero)

    """Acá se realizan los movimientos hasta que este ordenado o que el usuario decida salir"""
    while True:
        direcciones_usuario=verificar_direcciones(alto_tablero,ancho_tablero)
        if direcciones_usuario!="e":
            realizar_movimientos(tablero_usuario,direcciones_usuario[0], direcciones_usuario[2])
            mostrar_tablero(tablero_usuario,alto_tablero,ancho_tablero)
            if sixteen.esta_ordenado(tablero_usuario)==True:
                print("Has ganado el juego")
                return False
            else:
                continue
        else:
            print("Usted ha terminado el juego")
            return False 
main()
