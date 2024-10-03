#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <stdio.h>
#define CANT 5

char* pedir_palabra(){
    char input[CANT];
    printf("Ingrese una palabra: \n");
    fgets(input,sizeof(input),stdin);
    return input;
}
char* pedir_palabra2(){
    char input[CANT];
    printf("Ingrese una palabra: \n");
    fgets(input,sizeof(input),stdin);
    return input;
}
int main(){
    char* palabra1=pedir_palabra();
    char* palabra2=pedir_palabra2();
    int longitudes=strlen(palabra1)+strlen(palabra2);
    printf("%s",palabra1);
    for (int i=0;i<=(30-longitudes);i++){
        printf(".");
    }
    printf("%s\n",palabra2);
    return 0;
}