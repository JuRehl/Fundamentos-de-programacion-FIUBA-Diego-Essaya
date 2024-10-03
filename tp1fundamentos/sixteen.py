ITERACIONES_RANDOM=101
"""
Logica del juego Sixteen
"""
import random


def crear_tablero(n_filas: int, n_columnas: int) -> list[list[int]]:
    """
    Crea un tablero ordenado, con dimensiones `n_filas` por `n_columnas`.

    El tablero estará representado como una lista de listas de enteros. El
    primer número en la posición `[0][0]` será un 1, el de la izquierda será un
    2, y así sucesivamente hasta completar todos los casilleros, sin repetir
    los números, hasta llegar al número `n_filas * n_columnas`.

    PRECONDICIONES:
        - `n_filas` y `n_columnas` son enteros positivos mayor a uno y menores
        a diez.

    POSTCONDICIONES:
        - la función devuelve un nuevo tablero ordenado de enteros que se puede
        utilizar para llamar al resto de las funciones del módulo.

    EJEMPLO:
        >>> crear_tablero(4, 5)
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
        ]
    """
    
    tablero=[]
    inicio_columnas=1
    columnas=n_columnas
    for f in range (n_filas):
        fila=[]
        for c in range (inicio_columnas,columnas+1):
            fila.append(c)
        tablero.append(fila)
        inicio_columnas+=n_columnas
        columnas+=n_columnas
    return tablero


def rotar_izquierda(tablero: list[list[int]], fila: int) -> bool:
    """Rota la fila del tablero, indicada por el índice `fila`, hacia la
    izquierda.

    Por ejemplo, con `fila=1` y `tablero` como a la izquierda, al finalizar
    la función se modificará el tablero para que quede como en la derecha.
    [[1, 2, 3],           [[1, 2, 3],
     [4, 5, 6],    ==>     [5, 6, 4],
     [7, 8, 9]]            [7, 8, 9]]

    PRECONDICIONES:
        - `tablero` es una lista de lista de enteros de cualquier dimensión.

    POSTCONDICIONES:
        - Si `fila` es un índice de filas válido, la función realiza la
        rotación modificando el tablero y devuelve `True`.
        Caso contrario, no modifica el tablero y devuelve `False`."""
    if fila<len(tablero) and fila>=0:
        fila_escogida=tablero[fila]
        fila_escogida.insert(len(fila_escogida),fila_escogida.pop(0))
        return True
    return False
             




def rotar_derecha(tablero: list[list[int]], fila: int) -> bool:
    """Rota la fila del tablero, indicada por el índice `fila`, hacia la
    derecha.

    Por ejemplo, con `fila=1` y `tablero` como a la izquierda, al finalizar
    la función se modificará el tablero para que quede como en la derecha.
    [[1, 2, 3],           [[1, 2, 3],
     [4, 5, 6],    ==>     [6, 4, 5],
     [7, 8, 9]]            [7, 8, 9]]

    PRECONDICIONES:
        - `tablero` es una lista de lista de enteros de cualquier dimensión.

    POSTCONDICIONES:
        - Si `fila` es un índice de filas válido, la función realiza la
        rotación modificando el tablero y devuelve `True`.
        Caso contrario, no modifica el tablero y devuelve `False`."""
    if fila<len(tablero) and fila>=0:
        fila_escogida=tablero[fila]
        fila_escogida.insert(0,fila_escogida.pop())
        return True
    return False


def rotar_arriba(tablero: list[list[int]], columna: int) -> bool:
    """Rota la columna del tablero, indicada por el índice `columna`, hacia
    arriba.

    Por ejemplo, con `columna=1` y `tablero` como a la izquierda, al finalizar
    la función se modificará el tablero para que quede como en la derecha.
    [[1, 2, 3],           [[1, 5, 3],
     [4, 5, 6],    ==>     [4, 8, 6],
     [7, 8, 9]]            [7, 2, 9]]

    PRECONDICIONES:
        - `tablero` es una lista de lista de enteros de cualquier dimensión.

    POSTCONDICIONES:
        - Si `columna` es un índice de columnas válido, la función realiza la
        rotación modificando el tablero y devuelve `True`.
        Caso contrario, no modifica el tablero y devuelve `False`."""
    
    if columna<len(tablero[0]) and columna>=0:
        primer_numero=tablero[0][columna]
        for i in range(len(tablero)-1):
            tablero[i][columna]=tablero[i+1][columna]
        tablero[-1][columna]=primer_numero
        return True
    return False


def rotar_abajo(tablero: list[list[int]], columna: int) -> bool:
    """Rota la columna del tablero, indicada por el índice `columna`, hacia
    abajo.

    Por ejemplo, con `columna=1` y `tablero` como a la izquierda, al finalizar
    la función se modificará el tablero para que quede como en la derecha.
    [[1, 2, 3],           [[1, 8, 3],
     [4, 5, 6],    ==>     [4, 2, 6],
     [7, 8, 9]]            [7, 5, 9]]

    PRECONDICIONES:
        - `tablero` es una lista de lista de enteros de cualquier dimensión.

    POSTCONDICIONES:
        - Si `columna` es un índice de columnas válido, la función realiza la
        rotación modificando el tablero y devuelve `True`.
        Caso contrario, no modifica el tablero y devuelve `False`."""
    if columna<len(tablero[0]) and columna>=0:
        ultimo_numero=tablero[-1][columna]
        for i in range(len(tablero)-1,0,-1):
            tablero[i][columna]=tablero[i-1][columna]
        tablero[0][columna]=ultimo_numero
        return True
    return False


def esta_ordenado(tablero: list[list[int]]) -> bool:
    """
    Indica si los elementos del tablero se encuentran ordenados de izquierda a
    derecha, arriba a abajo, con el primer elemento siendo un 1 y cada elemento
    subsecuente incrementando su valor por uno.
    Por ejemplo, todo tablero que devuelva `crear_tablero` empieza ordenado.

    PRECONDICIONES:
        - `tablero` es una lista de lista de enteros de cualquier dimensión.
        - Los elementos de `tablero` no tienen números repetidos.
    """
    tablero_ordenado=crear_tablero((len(tablero)), len(tablero[0]))
    return tablero_ordenado==tablero
   

def mezclar_tablero(tablero: list[list[int]]):
    """
    Realiza ITERACIONES_RANDOM movimientos aleatorios al juego, siendo un
    movimiento cualquiera de las cuatro rotaciones sobre cualquier índice
    respectivo.

    PRECONDICIONES:
        - `tablero` es una lista de lista de enteros de cualquier dimensión.
    """
    
    for movimientos in range(ITERACIONES_RANDOM):
        fila_random=random.randint(0,len(tablero)-1)
        fila_random1=random.randint(0,len(tablero)-1)
        columna_random=random.randint(0,len(tablero[0])-1)
        columna_random1=random.randint(0,len(tablero[0])-1)
        movimiento=random.randint(1,4)
        if movimiento==1:
            rotar_izquierda(tablero,fila_random)
        elif movimiento==2:
            rotar_derecha(tablero,fila_random1)
        elif movimiento==3:
            rotar_arriba(tablero,columna_random)
        else:
            rotar_abajo(tablero,columna_random1)
        movimiento=0
    