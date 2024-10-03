#Parte 5

from vectores import norma,diferencia,prod_vect_r3

def area_triángulo(Ax,Ay,Az,Bx,By,Bz,Cx,Cy,Cz):
    """Le doy tres puntos de r3 y me calcula el area del triangulo"""
    #Resta para dar el vector AB y el vector AC
    diferencia_ABx,diferenciaABy,diferencia_ABz= diferencia(Ax,Ay,Az,Bx,By,Bz)
    diferencia_ACx,diferencia_ACy,diferencia_ACz= diferencia(Ax,Ay,Az,Cx,Cy,Cz)
    #Producto vectorial entre AB y AC
    prod_vectorialx,prod_vectorialy,prod_vectorialz=prod_vect_r3(diferencia_ABx,diferenciaABy,diferencia_ABz,diferencia_ACx,diferencia_ACy,diferencia_ACz)
    #Norma del producto vectorial
    norma_del_prod_vect= norma(prod_vectorialx,prod_vectorialy,prod_vectorialz)
    #Se divide la norma por 2 para darme el area del triángulo
    area= norma_del_prod_vect/2
    return area

assert area_triángulo(2,5,8,2,0,1,4,9,7)==18.607794065928395
assert area_triángulo(8,8,5,6,7,9,1,1,4)==21.15419580130618
assert area_triángulo(1,0,1,2,5,1,0,0,2)==3.570714214271425



    