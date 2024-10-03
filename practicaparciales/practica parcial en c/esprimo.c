#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <stdio.h>
#define CANT 5

int pedir_numero(){
    char input[CANT];
    while (true){
        printf("Ingrese un número: \n");
        fgets(input,sizeof(input),stdin);
        int num=atoi(input);
        if (num==0){
            continue;
        }
        return num;
    }
} 
bool es_primo(int num){
    if (num<=1){
        return false;
    }
    for (int i=2;i*i<=num;i++){
        if (num%i==0){
            return false;
        }
    }
    return true;
}
int main(){
    int num=pedir_numero();
    if (es_primo(num)){
        printf("El número %d es primo\n", num);
    }else{
        printf("El número %d no es primo\n", num);
    }
    return 0;
}