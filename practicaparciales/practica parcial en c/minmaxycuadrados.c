#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <stdio.h>
#define CANT 5

int cuadrados(int minimo,int maximo, int n){
    int cuadrado;
    for (int i=minimo;i<=maximo;i+=n){
        cuadrado=i*i;
        printf("%d  %d\n",i,cuadrado);
    }
    return 0;
}
int pedir_num(){
    char input[CANT];
    printf("Ingrese un numero: \n");
    fgets(input,sizeof(input),stdin);
    int num=atoi(input);
    return num;
}

int main(){
    int min=pedir_num();
    int max=pedir_num();
    int n=pedir_num();
    cuadrados(min,max,n);
    return 0;
}