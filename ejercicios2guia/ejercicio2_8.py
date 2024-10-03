#funcion que le doy un numero y calcula su factorial
def main():
    veces=int(input("Ingrese un número: "))
    resultado = 1
    for n in range (1,veces+1):
        num=int(input("Ingrese un número: "))
        for i in range(1,num+1):
            resultado = resultado*i
            print(i,"|",resultado)
    
main()