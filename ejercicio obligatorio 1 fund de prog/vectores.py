def norma(x,y,z):
    """Recibe un vector en R3 y devuelve su norma"""
    return (x**2 + y**2 + z**2) ** 0.5

def diferencia(x1,y1,z1,x2,y2,z2):
    """Recibe las coordenadas de dos vectores en R3 y devuelve su diferencia"""
    #Modifique, en vez de x1-x2 lo cambie a x2-x1, para hacer los vectores ab y ac del area del triángulo 
    dif_x = x2 - x1
    dif_y = y2 - y1
    dif_z = z2 - z1
    return dif_x, dif_y, dif_z


def prod_vect_r3(x1,y1,z1,x2,y2,z2):
    """Recibe las coordenadas de dos vectores en R3 y devuelve el producto vectorial"""
    parte_i = y1*z2 - z1*y2
    parte_j = z1*x2 - x1*z2
    parte_k = x1*y2 - y1*x2
    return parte_i, parte_j, parte_k