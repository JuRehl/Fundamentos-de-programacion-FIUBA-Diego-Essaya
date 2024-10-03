#include  <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

double norma_arreglo(int *arr, int longitud){
    int adentro_raiz=0;
    int elemento_al_cuadrado;
    for (int i=0;i<longitud;i++){
        elemento_al_cuadrado=arr[i]*arr[i];
        adentro_raiz+=elemento_al_cuadrado;
    }
    double resultado=sqrt((double)adentro_raiz);
    return resultado;
}
int main(){
    int nums[]={1,2,3,4};
    double norma=norma_arreglo(nums,4);
    printf("%f\n",norma);
    return 0;
}