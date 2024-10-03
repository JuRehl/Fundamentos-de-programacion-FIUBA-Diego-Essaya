#include "vector.h"
#include <stdbool.h>


vector_t *vector_crear(size_t tam) {
    if(tam==0)return NULL;
    vector_t* vector=malloc(sizeof(vector_t));
    if (vector==NULL){
        return NULL;
    }
    vector->valores=malloc(sizeof(int)*tam);
    if (vector->valores==NULL){
        free(vector);
        return NULL;
    }
    vector->tam=tam;
    return vector;
}

void vector_destruir(vector_t* vector) {
    free(vector->valores);
    free(vector);
}

bool vector_guardar(vector_t *vector, size_t pos, int valor) {
    if (pos<vector->tam){
        vector->valores[pos]=valor;
        return true;
    }
    return false;
}

bool vector_obtener(vector_t *vector, size_t pos, int *valor) {
    if (pos>=vector->tam){
        return false;
    }
    *valor=vector->valores[pos];
    return true;
}

size_t vector_largo(vector_t *vector) {
    return vector->tam;
}

void vector_por_escalar(vector_t *vector, int k) {
    for (size_t i=0;i<vector->tam;i++){
        vector->valores[i]=vector->valores[i]*k;
    }
}

vector_t* vector_sumar(vector_t *vector1, vector_t *vector2) {
    vector_t* vector_nuevo=malloc(sizeof(vector_t));
    if(vector_nuevo==NULL || vector1->tam!=vector2->tam){
        return NULL;
    }
    vector_nuevo->valores=malloc(sizeof(int)*vector1->tam);
    if(vector_nuevo->valores==NULL){
        free(vector_nuevo);
        return NULL;
    }
    for (size_t i=0;i<vector1->tam;i++){
        vector_nuevo->valores[i]=vector1->valores[i]+vector2->valores[i];
    }
    vector_nuevo->tam=vector1->tam;
    return vector_nuevo;
}

bool vector_redimensionar(vector_t *vector, size_t nuevo_tam) {
    if (nuevo_tam==0) return false;
    int *nuevo_espacio=malloc(sizeof(int)*nuevo_tam);
    if (nuevo_espacio==NULL){
        return false;
    }
    for (size_t i=0;i<nuevo_tam;i++){
        if (i>=vector->tam){
            nuevo_espacio[i]=0;
        }else{
            nuevo_espacio[i]=vector->valores[i];
        }
    }
    free(vector->valores);
    vector->valores=nuevo_espacio;
    vector->tam=nuevo_tam;
    return true;
}
