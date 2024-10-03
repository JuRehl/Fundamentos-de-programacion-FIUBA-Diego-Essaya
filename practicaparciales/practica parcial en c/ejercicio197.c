#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <stdio.h>
#define CANT 50

int adivinar_numero(int n){
    size_t contador=0;
    char input[CANT];
    while (true){
        printf("Ingrese un numero\n");
        fgets(input,sizeof(input),stdin);
        int num=atoi(input);
        if (num<n){
            printf("El numero es mayor a %d\n",num);
            contador++;
            continue;
        }
        else if(num>n){
            printf("El número es menor a %d\n", num);
            contador++;
            continue;
        }else{
            printf("Felicidades adivinaste en %zu intentos\n", contador);
            break;
        }
    }
    return contador;
}
int main(){
    int n=5;
    adivinar_numero(n);
    return 0;
}