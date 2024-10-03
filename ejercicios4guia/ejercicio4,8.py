def main():
    def calcular_signo():
        """Le doy una fecha y me dice su signo"""
        dia= int(input("Ingrese el día en que nacio: "))
        mes= int(input("Ingrese el mes en que nació: "))
        if mes==1:
            if dia>=1 and dia<=20:
                print( "Su signo es capricornio")
            else:
                print("Su signo es acuario")
        elif mes==2:
            if dia>=1 and dia<=19:
                print("Su signo es acuario")
            else:
                print("Su signo es piscis")
        elif mes==3:
            if dia>=1 and dia<=20:
                print("Su signo es piscis")
            else:
                print("Su signo es aires")
        elif mes==4:
            if dia>=1 and dia<=20:
                print("Su signo es aries")
            else:
                print("Su signo es tauro")
        elif mes==5:
            if dia>=1 and dia<=20:
                print("Su signo es tauro")
            else:
                print("Su signo es géminis")
        elif mes==6:
            if dia>=1 and dia<=21:
                print("Su signo es géminis")
            else: 
                print("Su signo es cáncer")
        elif mes==7:
            if dia>=1 and dia<=23:
                print("Su signo es cáncer")
            else:
                print("Su signo es leo")
        elif mes==8:
            if dia>=1 and dia<=23:
                print("Su signo es leo")
            else:
                print("Su signo es virgo")
        elif mes==9:
            if dia>=1 and dia<=23:
                print("Su signo es virgo")
            else: 
                print("Su signo es libra")
        elif mes==10:
            if dia>=1 and dia<=22:
                print("Su signo es libra")
            else: 
                print("Su signo es escorpio")
        elif mes==11:
            if dia>=1 and dia<=22:
                print("Su signo es escorpio")
            else:
                print("Su signo es sagitario")
        else:
            if dia>=1 and dia<=21:
                print("Su signo es sagitario")
            else:
                print("Su signo es capricornio")
    calcular_signo()
main()