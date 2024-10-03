OPCION_SALIDA= "exit"
def main():
    notas= 0
    cant_notas=0
    while True:
        nota= input("Ingrese una nota, si ya ingreso todas escribe exit: ")
        if nota==OPCION_SALIDA:
            break
        notas+=float(nota)
        cant_notas+=1
    if cant_notas==0:
        print("El promedio es 0")
    else:
        print("El promedio de las notas es: ", notas/cant_notas)
    
main()