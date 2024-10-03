CONTRASEÑA="juana"
#Ejercicio 5.3 a
def main():
    """le doy una contraseña y me la valida hasta que sea la correcta"""
    contraseña_usuario=input("Ingrese la contraseña: ")
    while contraseña_usuario!=CONTRASEÑA:
        print("Contraseña inválida")
        contraseña_usuario=input("Ingrese la contraseña: ")
    print("Contraseña correcta")
main()

#Ejercicio 5.3 b
def main():
    """Le doy una contraseña y me deja validarla hasta 4 intentos"""
    contraseña_usuario=input("Ingrese la contraseña: ")
    contador=0
    while contador<=2:
        if contraseña_usuario!=CONTRASEÑA:
            print("Contraseña inválida")
            contraseña_usuario=input("Ingrese la contraseña: ") 
        contador+=1 
    if CONTRASEÑA==contraseña_usuario:
        print("Contraseña correcta")
    else:
        print("Se han acabado los intentos")
main()

#Ejercicio 5.3c 
def main():
    import time
    contraseña_usuario=input("Ingrese la contraseña: ")
    contador=1
    sleep=1
    time.sleep(sleep)
    while contador<=2:
        if contraseña_usuario!=CONTRASEÑA:
            print("Contraseña inválida")
            contraseña_usuario=input("Ingrese la contraseña: ") 
            sleep+=1
            time.sleep(sleep)
        contador+=1 
    if CONTRASEÑA==contraseña_usuario:
        print("Contraseña correcta")
    else:
        print("Se han acabado los intentos")   
        
main()

#Ejercicio 5.3 d
def main():
    import time
    contraseña_usuario=input("Ingrese la contraseña: ")
    contador=1
    sleep=1
    time.sleep(sleep)
    while contador<=2:
        if contraseña_usuario!=CONTRASEÑA:
            contraseña_usuario=input("Ingrese la contraseña: ") 
            sleep+=1
            time.sleep(sleep)
        contador+=1 
    if CONTRASEÑA==contraseña_usuario:
        return True
    else:
        return False
        
main()
