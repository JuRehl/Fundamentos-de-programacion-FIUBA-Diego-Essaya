#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <stdio.h>
#define CANT 50

bool es_primo(int n) {
    if (n <= 1) {
        return false;
    }
    for (int i = 2; i<n; i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int main(){
    char input[CANT];
    printf("Ingrese un entero: \n");
    fgets(input,sizeof(input),stdin);
    int num=atoi(input);
    int contador=0;
    int numero=2;
    while(true){
        if (es_primo(numero)==true){
            printf("%d ",numero);
            contador++;
            numero++;
            if (contador==num){
                printf("\n");
                break;
            }else{
                continue;
            }
        }else{
            numero++;
            continue;
        }
    }
    return 0;
}