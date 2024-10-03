#include <stdbool.h>
#include <stdio.h>

//Ejercicio 17;5
//comilla simple un caracter, comillas dobles arreglo de caracteres, cadenas terminan en /0
// #include <string.h>tiene una funcion de strlen 

size_t strlen(char*texto){
    size_t cant=0;
    while (texto[cant]!="\0"){
        cant++;
    }    
    return cant;
}

size_t strlen2(char*texto, int contador){
    if (texto[contador]=='\0'){
        return contador;
    }
    contador++;
    return strlen2(texto,contador);
}