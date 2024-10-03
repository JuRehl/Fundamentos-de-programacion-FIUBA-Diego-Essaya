#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <stdio.h>
#include <ctype.h>
#define CANT 100

int main(){
    char input[CANT];
    char nueva_cad[CANT];
    printf("Ingrese una cadena: \n");
    fgets(input,sizeof(input),stdin);
    for (size_t i=0;i<strlen(input);i++){
        if (isalpha(input[i])){
            nueva_cad[i]=input[i];
        }else{
            nueva_cad[i]=' ';
        }
    }
    printf("%s\n",nueva_cad);
    return 0;
}
