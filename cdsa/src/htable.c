#include "htable.h"

//
static unsigned int hash(const char *x){
    unsigned int h = 0U;
    for(int i=0; x[i] != '\0'; i++){
        h = h * 65599 + (unsigned char)x[i];
    }
    return h & 1023;
}
