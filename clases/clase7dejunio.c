#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// typedef struct Persona //son simplemente datos (ejemplo clase con solo elementos no atributos o funciones)
// {
//     char nombre[30];
//     int edad;
//     float altura;
// } persona_t;

// int main(){
//     persona_t pedro;
//     pedro.edad=34;
//     pedro.altura=1.83;
//     strcpy(pedro.nombre,"pedro");
//     printf("%s %d %f", pedro.nombre,pedro.edad,pedro.altura);
// }
typedef struct punto
{
    float x;
    float y;
} punto_t;

typedef struct plano
{
    punto_t* puntos;
    size_t capacidad;
    size_t cantidad;
}plano_t;

plano_t* plano_crear(size_t capacidad){
    plano_t* plano=malloc(sizeof(plano_t));
    if (plano==NULL){
        return NULL;
    }
    plano->capacidad=capacidad;
    plano->puntos=malloc(sizeof(punto_t)*capacidad);
    if (plano->puntos==NULL){
        free(plano);
        return NULL;
    }
    plano->cantidad=0;
    return plano;
}

bool plano_agregar(plano_t* plano,float x,float y){
    if (plano->capacidad==plano->cantidad)return false;
    size_t i=plano->cantidad;
    plano->puntos[i].x=x;
    plano->puntos[i].y=y;
    plano->cantidad++;
    return true;
}

bool plano_obtener_centroide(plano_t* plano, float *res_x,float *res_y){
    if (plano->cantidad==0)return false;
    float suma_x=0;
    float suma_y=0;
    for (size_t i=0;i<plano->cantidad;i++){
        suma_x+=plano->puntos[i].x;
        suma_y+=plano->puntos[i].y;
    }
    *res_x=suma_x/plano->cantidad;
    *res_y=suma_y/plano->cantidad;
    return true;
}

void plano_destruir(plano_t*plano){
    free(plano->puntos);
    free(plano);
}

int main(){
    plano_t* plano=plano_crear(50);
    plano_agregar(plano,7,9);
    plano_agregar(plano,-7,8);
    float x,y;
    plano_obtener_centroide(plano,&x,&y);
    printf("%f %f\n",x,y);
    plano_destruir(plano);
}