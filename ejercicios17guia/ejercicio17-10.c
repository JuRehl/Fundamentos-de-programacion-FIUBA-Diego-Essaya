#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

void imprimir(char *cadena){
    int cantidad=strlen(cadena)+4;
    for (int i=0;i<cantidad;i++){
        printf("*");
    }
    printf("\n");
    printf("* %s *\n",cadena);
    for (int n=0;n<cantidad;n++){
        printf("*");
    }
    printf("\n");
}
int main(){
    char cadena[]="Lenguaje C";
    imprimir(cadena);
    return 0;
}


