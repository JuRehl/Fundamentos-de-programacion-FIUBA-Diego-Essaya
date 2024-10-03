#Ejercicio 6.5 a
def primeras_letras(frase):
    """te da las iniciales de una frase"""
    palabras= frase.split()
    iniciales=[palabra[0]for palabra in palabras]
    return "".join(iniciales)
primeras_letras("Universal Serial Bus")

#Ejercicio 6.5 b
def mayusculas_palabras(frase):
    """Te pone en mayusculas la primera letra de cada palabra"""
    return frase.title()
mayusculas_palabras("republica argentina")

#Ejercicio 6.5 c
def palabras_que_comienzan_con_a(frase):
    """te devuelve las palabras q comienzan con a"""
    palabras=frase.split()
    nueva_frase=[]
    for palabra in palabras:
        if palabra.startswith("a"):
            nueva_frase.append(palabra)
    final=" ".join(nueva_frase)
    print(final)
palabras_que_comienzan_con_a("antes de ayer")