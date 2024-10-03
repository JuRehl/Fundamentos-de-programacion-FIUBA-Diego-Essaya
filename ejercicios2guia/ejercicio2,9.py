def main():
    def mostrar_coords (columnas: int, filas: int) -> None:
        """Imprime matriz con todas las coordenadas"""
        for i in range (filas+1):
            for c in range (columnas+1):
                print(str(i) + "," + str(c), end= "  ")
        print()
    mostrar_coords(6,6)

main()
