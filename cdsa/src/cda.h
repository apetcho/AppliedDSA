#ifndef __CDA__H
#define __CDA__H
#include<assert.h>
#include<string.h>
#include<stdlib.h>

#define CDA_TRUE            1
#define CDA_FALSE           0
#define CDA_ASSERT(expr)    (assert(exp))
#define CDA_CARD(arr)       (sizeof((arr))/sizeof(*(arr)))
#define CDA_NEW(type)       ((type*)CDA_malloc(sizeof(type)))
#define CDA_NEW_STR(str)    \
    (strcpy((char*)CDA_malloc(strlen((str))+1), (str)))
#define CDA_NEW_STR_IF(str) \
    ((str) == NULL ? NULL : CDA_NEW_STR((str)))

typedef int cda_bool_t;
typedef signed char cda_int8_t;
typedef unsigned char cda_uint8_t;



void* CDA_malloc(size_t size){
    assert(size > 0);
    void *mem = malloc(size);
    if(mem == NULL){ abort(); }
    return mem;
}

void CDA_free(void *mem){
    if(mem != NULL){free(mem);}
}

#endif
