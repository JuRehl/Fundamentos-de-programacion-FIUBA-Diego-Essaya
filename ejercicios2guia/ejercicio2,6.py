def main():
    #Te muestra los numeros pares entre los numeros dados
    num1=int(input("Ingrese un numero: "))
    num2=int(input("Ingrese otro numero: "))
    for i in range(num1,num2+1):
        if (i%2==0):
            print(i)
main()