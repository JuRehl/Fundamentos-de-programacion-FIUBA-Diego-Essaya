#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include<stdlib.h>
#define CANT 50

int pedir_invertir_cadena(){
    char input[CANT];
    printf("Ingrese una cadena: \n");
    fgets(input,sizeof(input),stdin);
    int longitud=strlen(input);
    for (int i=0;i<(longitud/2);i++){
        char aux=input[longitud-i-1];
        input[longitud-1-i]=input[i];
        input[i]=aux;
    }
    printf("%s\n",input);
    return 0;
}
int main(){
    pedir_invertir_cadena();
    return 0;
}