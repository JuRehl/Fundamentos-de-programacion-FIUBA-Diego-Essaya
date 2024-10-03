VOCALES="AaEeIiOoUu"
#Ejercicio6.6 a
def palabras_sin_vocales(palabra):
    """te saca las vocales de una palabra"""
    letras=list(palabra)
    letras_consonantes=[]
    for letra in letras:
        if not letra in VOCALES:
            letras_consonantes.append(letra)
    final=" ".join(letras_consonantes)
    return final
palabras_sin_vocales("algoritmos")

#Ejercicio 6.6 b
def palabras_solo_vocales(palabra):
    """te saca las consonantes de una frase o palabra"""
    letras=list(palabra)
    letras_consonantes=[]
    for letra in letras:
        if  letra in VOCALES:
            letras_consonantes.append(letra)
    final=" ".join(letras_consonantes)
    return final
palabras_solo_vocales("Sin consonantes")

#Ejercicio 6.6 c
def palabra_vocal_siguiente(palabra):
    vocales2=["e","i","o","u","a"]
    palabra_nueva=""
    for letra in palabra:
        if letra in vocales2:
            palabra_nueva+=vocales2[palabra.index(letra)+1]
        else:
            palabra_nueva+=letra
    print(palabra_nueva)
palabra_vocal_siguiente("vestuario")