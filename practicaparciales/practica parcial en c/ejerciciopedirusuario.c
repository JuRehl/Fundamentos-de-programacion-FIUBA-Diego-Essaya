#include  <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#define CANT 10

int pedir_numero(char *msj, int min, int max){
    char input[CANT];
    while (true){
        printf("%s [%d,%d]: ", msj,min,max);
        fgets(input,sizeof(input),stdin);
        int num= atoi(input);
        if (num==0){
            printf("Ingrese un número correcto\n");
            continue;
        }
        if (num>max || num<min){
            printf("Ingrese un número correcto\n");
            continue;
        }
        return num;
    }
}
int main(){
    char msj[]="Numero";
    int max=9;
    int min=0;
    pedir_numero(msj,min,max);
}

