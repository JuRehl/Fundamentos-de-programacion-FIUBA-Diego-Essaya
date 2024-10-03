import os
import auxiliares
MAXIMO_IMPRESION=15.0
MAXIMO_GUARDADO=1.0
FORMATO_ARCHIVOS=".txt"

def main():
    archivos=[]
    lista_archivos_verificada=[]
    dicc_nuevo={}
    while True:
        ruta_previsoria=auxiliares.verificar_ruta()
        if ruta_previsoria==auxiliares.SALIDA:
            break
        ruta=ruta_previsoria
        N = auxiliares.verificar_N()
        lista_archivos=os.listdir(ruta)
        for n in lista_archivos:
            if n[-4:]==FORMATO_ARCHIVOS:
                lista_archivos_verificada.append(n)
            else:
                continue
        for archivo in lista_archivos_verificada:
            archivo=os.path.join(ruta,archivo)
            archivos.append(archivo)
        dicc_resultados=auxiliares.comparar_archivos(archivos,N)
        dicc_nuevo=auxiliares.limpiar_claves(dicc_resultados)
        print("Resultados sospechosos:")
        contador=1
        for key in dicc_nuevo:
            if dicc_nuevo[key]>=MAXIMO_IMPRESION:
               archivo1,archivos2=key
               print(f"{contador}. {archivo1} vs {archivos2} ({dicc_nuevo[key]}%)")
               contador+=1
        ruta_destino=input("Ingrese un archivo para guardar los resultados: ")
        with open(ruta_destino,"w") as archivo_destino:
            archivo_destino.write("nombre_archivo1,nombre_archivo2,similaridad"+"\n")
            for k in dicc_nuevo:
                if dicc_nuevo[k]>MAXIMO_GUARDADO:
                    result=dicc_nuevo[k]
                    arch1,arch2=k
                    archivo_destino.write(f"{arch1},{arch2},{result}%"+"\n")
main()