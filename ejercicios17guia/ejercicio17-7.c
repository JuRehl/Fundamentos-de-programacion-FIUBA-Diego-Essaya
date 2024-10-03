#include <string.h>
//ejrecicio 17;7

char* strcpy(char* dst,char* org){
    for (size_t i=0;i<strlen(org)+1;i++){
        dst[i]=org[i]; //la cadena se modifica in-place
    }
    dst[strlen(org)]='\0';
    return dst;
}