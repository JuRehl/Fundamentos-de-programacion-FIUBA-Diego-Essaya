#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <stdio.h>

int imprimir_slogan(char *nombre, int N){
    char primeras_dos[3];
    char letra_repetida[2+N];
    int contador=2;
    for (int i=0;i<2;i++){
        primeras_dos[i]=nombre[i];
    }
    letra_repetida[0]=primeras_dos[0];
    letra_repetida[1]=primeras_dos[1];
    for (int j=0; j<N;j++){
        letra_repetida[contador]=letra_repetida[1];
        contador++;
    }
    for (int f=0;f<N;f++){
        printf("%s, ",primeras_dos);
    }
    printf("%s %s\n6",nombre,letra_repetida);
    return 0;
}
int main(){
    char xd[]="Simona";
    int n=3;
    imprimir_slogan(xd,n);
    return 0;
}