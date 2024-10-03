#Ejercicio 4.5 a
def año_bisiesto(año):
    """Te dice si el año es bisiesto"""
    if año%4!=0:
        return(False)
    if año%100!=0:
        return(True)
    if año%400!=0:
        return(False)
    return(True)

#Ejercicio 4.5 b

#Ejercicio 4.5 c
def fecha(dia,mes,año):
    """Le doy una fecha me dice si es válida o no"""
    if (0<dia<32) and (0<mes<13) and (año<2025):
        return True
    else:
        return False
fecha(50,2,2021)

#Ejercicio 4.5 d
def fecha_fin_mes(dia,mes):
    """Le doy un dia y me dice cuanto falta para terminar el mes"""
    meses_31= 1, 3, 5, 7, 8 , 10, 12
    meses_30=4, 6, 9, 11
    meses_28= 2 
    if mes in meses_31:
        print("Faltan ", (31-dia), "dias para finalizar el mes")
    elif mes in meses_30:
        print("Faltan ", (30-dia), "dias para finalizar el mes")
    else:
        print("Faltan", (28-dia), "dias para terminar el mes")
fecha_fin_mes(7,6)

#Ejercicio 4.5 e
def dias_fin_año (dia, mes):
    """Le doy una fecha y e dice cuant falta para fin de año"""
    if mes==1:
        print("Para fin de año faltan ", 365-dia, "dias")
    elif mes==2:
        dias_totales=dia +31
        print("Para fin de año faltan ", 365-dias_totales, "dias")
    elif mes==3:
        dias_totales=dia +31 +28
        print("Para fin de año faltan ", 365-dias_totales, "dias")
    elif mes==4:
        dias_totales=dia+ (31*2)+28
        print("Para fin de año faltan ", 365-dias_totales, "dias")
    elif mes==5:
        dias_totales=dia+(31*2)+30+28
        print("Para fin de año faltan ", 365-dias_totales, "dias")
    elif mes==6:
        dias_totales=dia+(31*3)+30+28
        print("Para fin de año faltan ", 365-dias_totales, "dias")
    elif mes==7:
        dias_totales=dia+(31*3)+(30*2)+28
        print("Para fin de año faltan ", 365-dias_totales, "dias")
    elif mes==8:
        dias_totales=dia+(31*4)+(30*2)+28
        print("Para fin de año faltan ", 365-dias_totales, "dias")
    elif mes==9:
        dias_totales=dia+(31*5)+(30*2)+28
        print("Para fin de año faltan ", 365-dias_totales, "dias")
    elif mes==10:
        dias_totales=dia+(31*5)+(30*3)+28
        print("Para fin de año faltan ", 365-dias_totales, "dias")
    elif mes==11:
        dias_totales=dia+(31*6)+(30*3)+28
        print("Para fin de año faltan ", 365-dias_totales, "dias")
    elif mes==12:
        dias_totales= dia+(31*6)+(30*4)+28
        print("Para fin de año faltan ", 365-dias_totales, "dias")
    else: 
        print("Ingrese un mes válido")
dias_fin_año(25,12)

#Ejercicio 4.5 f
def dias_hasta_fecha(dia,mes):
    """Le doy una fecha y me dice cuant falta para fin de año"""
    if mes==1:
        print("Del año transcurrieron ", dias_totales, "dias")
    elif mes==2:
        dias_totales=dia +31
        print("Del año transcurrieron ", dias_totales, "dias")
    elif mes==3:
        dias_totales=dia +31 +28
        print("Del año transcurrieron ", dias_totales, "dias")
    elif mes==4:
        dias_totales=dia+ (31*2)+28
        print("Del año transcurrieron ", dias_totales, "dias")
    elif mes==5:
        dias_totales=dia+(31*2)+30+28
        print("Del año transcurrieron ", dias_totales, "dias")
    elif mes==6:
        dias_totales=dia+(31*3)+30+28
        print("Del año transcurrieron ", dias_totales, "dias")
    elif mes==7:
        dias_totales=dia+(31*3)+(30*2)+28
        print("Del año transcurrieron ", dias_totales, "dias")
    elif mes==8:
        dias_totales=dia+(31*4)+(30*2)+28
        print("Del año transcurrieron ", dias_totales, "dias")
    elif mes==9:
        dias_totales=dia+(31*5)+(30*2)+28
        print("Del año transcurrieron ", dias_totales, "dias")
    elif mes==10:
        dias_totales=dia+(31*5)+(30*3)+28
        print("Del año transcurrieron ", dias_totales, "dias")
    elif mes==11:
        dias_totales=dia+(31*6)+(30*3)+28
        print("Del año transcurrieron ", dias_totales, "dias")
    elif mes==12:
        dias_totales= dia+(31*6)+(30*4)+28
        print("Del año transcurrieron ", dias_totales, "dias")
    else: 
        print("Ingrese un mes válido")
dias_hasta_fecha(26,12)
