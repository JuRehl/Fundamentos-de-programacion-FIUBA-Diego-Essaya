#Ejercicio 6.4
def separar_cada_3_digitos(numero,digito,intervalo):
    """Te separa cada millones"""
    parte=[numero[max(i+intervalo,0):i] for i in range(len(numero),0 ,-3)]
    print(digito.join(parte[::-1]))
separar_cada_3_digitos("1234567890", ".",-3)