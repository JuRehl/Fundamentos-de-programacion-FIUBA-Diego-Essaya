#Ejercicio 7.10 a
def sumar_matrices(m1,m2):
    resultado=[]
    for i in range(len(m1)):
        fila=[]
        for j in range(len(m1[0])):
            fila.append(m1[i][j]+m2[i][j])
        resultado.append(fila)
    return resultado
#otra forma
def sumar(m1,m2):
    for i in range(len(m1)):
        for j in range(len(m1[i])):
            m1[i][j]+=m2[i][j]

#Ejercicio 7.10 b
def multiplicar_matrices(m1,m2):
    resultadofinal=[]
    resultado=[]
    for i in range(len(m1)):
        for j in range(len(m1[i])):
            resultadoparcial=[]
            resultadoparcial=(m1[i][j]*m2[0][1])
        resultado.append(resultadoparcial)
    resultadofinal.append(resultado)
    return resultadofinal
m1ej=[[2,3],[1,2]]
m2ej=[[4,5],[2,1]]
print(multiplicar_matrices(m1ej,m2ej) )       
    


            