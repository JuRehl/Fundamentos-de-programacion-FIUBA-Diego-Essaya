def main():
    palabra=str(input("Ingrese una palabra: "))
    #le doy una palabra y me la imprime 1000 veces seguidas
    for i in range (0,1001):
        print(palabra, end=" ")
        i+=1
main()
