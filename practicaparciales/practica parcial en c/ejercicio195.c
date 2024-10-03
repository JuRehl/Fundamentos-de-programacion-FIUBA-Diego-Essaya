#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <stdio.h>
#define CANT 50

int main(){
    char input[CANT];
    while (true){
        printf("Ingrese un entero: \n");
        fgets(input,sizeof(input),stdin);
        int num=atoi(input);
        if (num<1){
            printf("Ingrese un número correcto\n");
            continue;
        }else{
            for (int i=0;i<num+1;i++){
                for(int j=0;j<i;j++){
                    printf("*");
                }
                printf("\n");
            }
            break;
        }
    }
    return 0;
}