#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <stdio.h>
#define CANT 50

int cantidad_num(int*arr,int largo,int num){
    int contador=0;
    for (int i=0;i<largo;i++){
        if (arr[i]==num){
            contador++;
        }
    }
    return contador;
}
int main(){
    char input[CANT];
    while (true){
        printf("Ingrese un entero: \n");
        fgets(input,sizeof(input),stdin);
        int num=atoi(input);
        if (num<1){
            continue;
        }else{
            int arreglo[]={1,2,3,4,5,5};
            int longitud=sizeof(arreglo)/sizeof(arreglo[0]);
            int cont=cantidad_num(arreglo,longitud,num);
            printf("El número %d aparece %d veces\n",num,cont);
            break;
        }
    }
    return 0;
}