#ejercicio 7.1
def ordenados_de_menor_a_mayor(tupla):
    """Le doy una tupla y me dice si esta ordenada de menor a mayor"""
    if tupla == tuple(sorted(list(tupla))):
        print("La tupla esta ordenada de menor a mayor")
    else:
        print("La tupla no esta ordenada de menor a mayor")
tupla_prueba=(5,4,2,8)
ordenados_de_menor_a_mayor(tupla_prueba)