#Ejercicio 5.5 a
def m_c_d(m,n):
    """Le doy dos números y me dice su máximo común divisor"""
    divisores=""
    if m%n==0:
        print("El mayor común divisor es ", n)
    else:
        for j in range (1,m+1):
            if n%j==0 and m%j==0:
                divisores= divisores+ str(j) +" "
                continue
        print("Los divisores son: ", divisores)
m_c_d(10,8)

        

