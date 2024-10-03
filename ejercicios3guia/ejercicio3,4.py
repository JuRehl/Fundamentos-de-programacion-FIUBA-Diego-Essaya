#Ejercicio 3.4 a
def norma(x, y, z):
    """Recibe un vector en R3 y devuelve su norma"""
    return (x**2 + y**2 + z**2) ** 0.5

assert norma(-60, -60, -70) == 110.0
assert norma(26, 94, -17) == 99.0
assert norma(34, 18, -69) == 79.0
assert norma(-34, 63, -42) == 83.0
assert norma(0, 35, 84) == 91.0
assert norma(6, -7, 6) == 11.0
assert norma(94, -3, -42) == 103.0
assert norma(0, 42, -40) == 58.0
assert norma(48, -33, 24) == 63.0
assert norma(0, 0, 0) == 0

#Ejercicio 3.4 b
z = 85
assert norma(-70, 14, z) == 111.0

def diferencia(x1, y1, z1, x2, y2, z2):
    """Recibe las coordenadas de dos vectores en R3 y devuelve su diferencia"""
    dif_x = x1 - x2
    dif_y = y1 - y2
    dif_z = z1 - z2
    return dif_x, dif_y, dif_z

# Agregar pruebas

assert diferencia(1, 2, 3, 1, 2, 3) == (0, 0, 0)
assert diferencia(16, -72, -52, 55, 90, -31) == (-39, -162, -21)
assert diferencia(55, -88, -75, 38, 62, -12) == (17, -150, -63)

#Ejercicio 3.4 c
def prod_vect_r3(x1, y1, z1, x2, y2, z2):
    """Recibe las coordenadas de dos vectores en R3 y devuelve el producto vectorial"""
    parte_i = y1*z2 - z1*y2
    parte_j = z1*x2 - x1*z2
    parte_k = x1*y2 - y1*x2
    return parte_i, parte_j, parte_k

assert prod_vect_r3(54, 12, 29, 1, 11, 12) == (-175, -619, 582)
assert prod_vect_r3(71, 52, 24, 1, 11, 6) == (48, -402, 729)
assert prod_vect_r3(726, 434, 110, 488, 962, 820) == (250060, -541640, 486620)
assert prod_vect_r3(62, 12, 198, 380, 334, 490) == (-60252, 44860, 16148)
assert prod_vect_r3(-85, 807, 964, 462, 101, 474) == (285154, 485658, -381419)
assert prod_vect_r3(746, 466, 396, 910, 138, 289) == (80026, 144766, -321112)
assert prod_vect_r3(-15, 53, 105, 413, 149, 270) == (-1335, 47415, -24124)
assert prod_vect_r3(291, 413, 227, 166, 638, 284) == (-27534, -44962, 117100)
assert prod_vect_r3(192, 362, 397, 249, 598, 50) == (-219306, 89253, 24678)
assert prod_vect_r3(781, 520, 996, 348, 68, 215) == (44072, 178693, -127852)
assert prod_vect_r3(459, 971, 201, 582, 569, 703) == (568244, -205695, -303951)
assert prod_vect_r3(754, 968, 956, 231, 901, -31) == (-891364, 244210, 455746)

#Ejercicio 3.4.d de la guía

def area_triángulo(Ax1,Ay1,Az1,Bx2,By2,Bz2,Cx3,Cy3,Cz3):
    """Le doy tres puntos y me calcula el area del triangulo"""
    #Resta para dar el vector AB y el vector AC
    difx_AB= Bx2 - Ax1
    dify_AB= By2 - Ay1
    difz_AB = Bz2 - Az1
    difx_AC = Cx3 - Ax1
    dify_AC = Cy3 - Ay1
    difz_AC = Cz3 - Az1
    #Producto vectorial entre AB y AC
    Prod_vectorial_i= dify_AB*difz_AC - difz_AB*dify_AC
    Prod_vectorial_j= difz_AB*difx_AC - difx_AB*difz_AC
    Prod_vectorial_k= difx_AB*dify_AC - dify_AB*difx_AC
    #Norma del producto vectorial
    norma= (Prod_vectorial_i**2 + Prod_vectorial_j**2 + Prod_vectorial_k**2) ** 0.5
    #Se divide la norma por 2 para darme el area del triángulo
    area= norma/2
    print("El area es: ", area)
    return(area)

assert area_triángulo(2,5,8,2,0,1,4,9,7)
assert area_triángulo(8,8,5,6,7,9,1,1,4)
assert area_triángulo(1,0,1,2,5,1,0,0,2)