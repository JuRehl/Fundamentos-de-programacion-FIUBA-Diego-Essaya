#Ejercicio 6.2 a
def separar_en_caracter(palabra,caracter):
    """Te separa cada letra con ,"""
    print(caracter.join(palabra))
separar_en_caracter("separar", ",")

#Ejercicio 6.2 b
def unir_cadena(frase,caracter):
    """Te une con _ en los espacios"""
    print(frase.replace(" ", caracter))
unir_cadena("mi archivo de texto.txt", "_")

#Ejercicio 6.2 c
def devolver_contra_x(contraseña, caracter):
    """devuelve en numero en x por cada digito"""
    print("Su contraseña es: ", contraseña)
    if contraseña.isdecimal()==True:
        for l in contraseña:
            contraseña= contraseña.replace(l,caracter)
        print("Su contraseña es: ", contraseña)
devolver_contra_x("1580", "x")

#Ejercicio 6.2 d
def separar_cada_3_digitos(numero,digito,intervalo):
    """te separa cada 3 digitos"""
    parte=[numero[i:i+intervalo] for i in range(0,len(numero), intervalo)]
    print(digito.join(parte))
separar_cada_3_digitos("2552552550", ".",3)


